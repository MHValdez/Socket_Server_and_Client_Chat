"""
Assignment:     Programming Project 4: Client / Server Chat
File:           Configuration
Description:    Configuration file for both server and client scripts.
                A list of constants.

Dependencies:   None

Course:         CS 372
Section:        400
Module:         10

Name:           Marcos Valdez
ONID:           valdemar

Due:            12/04/2022
Modified:       12/03/2022
"""

import random

HOST =      "127.0.0.1"                     # Standard loopback interface address (localhost)
PORT =      55085                           # Port to listen on (non-privileged ports are > 1023)
CLIENT =    random.randint(57344, 65535)    # Client port
BUFFER =    4096                            # Socket .recv buffer size
MIN_RESP =  18                              # Response size lower limit to close socket
