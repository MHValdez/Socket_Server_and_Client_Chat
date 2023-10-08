"""
Assignment:     Programming Project 4: Client / Server Chat
File:           Server
Description:    A single socket chat server program in the form of a function
                that is called when the file is run as a script. Creates a
                socket server on the local host and listens for a connection
                from a client. Receives/displays and sends messages in the IDE
                console until either host ends the chat.

Dependencies:   config.py
                client.py

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

def server():
    """
    A single socket chat server. Creates a socket server on
    the local host and listens for a connection from a client.
    Receives/displays and sends messages in the IDE console
    until either host ends the chat.

    Library dependencies:   socket, sys
    File dependecies:       config.py, client.py

    :return: None
    """
    host = config.HOST
    port = config.PORT
    buffer = config.BUFFER
    min_resp = config.MIN_RESP

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))

        # Listen for and accept connection
        s.listen()
        print(f'Server listening on: localhost on port: {port}')
        conn, addr = s.accept()

        with conn:
            print(f'Connected by {addr}')
            print('Waiting for message...')

            # Initialize chat interface
            prompt = True

            while True:
                # Receive and decode chat message
                response = conn.recv(buffer)
                content = response.decode()

                # Close connection if message is empty
                if sys.getsizeof(response) < min_resp:
                    conn.close()
                    s.close()
                    break

                # Display received chat message
                print(content)

                # Display chat prompt only for first reply
                if prompt:
                    print('Type /q to quit')
                    print('Enter message to send...')
                    prompt = False

                # Get input for reply
                message = input(">")

                if message == '/q':
                    # Close connection
                    break
                else:
                    # Send reply message
                    data = bytes(message, 'utf-8')
                    conn.sendto(data, addr)


if __name__ == '__main__':
    server()