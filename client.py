"""
Assignment:     Programming Project 4: Client / Server Chat
File:           Client
Description:    A single socket chat client program in the form of a function
                that is called when the file is run as a script. Connects to
                a socket server on the local host. Receives/displays and sends
                messages in the IDE console until either host ends the chat.

Dependencies:   config.py
                server.py

Course:         CS 372
Section:        400
Module:         10

Name:           Marcos Valdez
ONID:           valdemar

Due:            12/04/2022
Modified:       12/03/2022
"""

import config
import socket
import sys

def client():
    """
    A single socket chat client. Connects to a socket server
    on the local host. Receives/displays and sends messages
    in the IDE console until either host ends the chat.

    Library dependencies:   socket, sys
    File dependecies:       config.py, server.py

    :return: None
    """
    host = config.HOST
    port = config.PORT
    client = config.CLIENT
    buffer = config.BUFFER
    min_resp = config.MIN_RESP

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, client))

        # Connect to host
        s.connect((host, port))
        print(f'Connected to: localhost on port: {port}')
        print('Type /q to quit')
        print('Enter a message to send...')

        while True:
            # Get input for message
            message = input(">")

            if message == '/q':
                # Close connection
                break
            else:
                # Send message
                data = bytes(message, 'utf-8')
                s.sendto(data, (host, port))

            # Receive and decode chat message
            response = s.recv(buffer)
            content = response.decode()

            # Close connection if message is empty
            if sys.getsizeof(response) < min_resp:
                break

            # Display received chat message
            print(content)


if __name__ == '__main__':
    client()