#!/usr/bin/env python3

"""
A very basic script to leave messages for others in an IRC channel.

:author: tpltnt
:license: AGPLv3 (or later)
"""

import socket
import sys

# open a socket to talk to a freenode IRC server (in clear text)
try:
    # IRC is TCP, so the python defaults are fine
    connection = socket.create_connection(("chat.freenode.net", 6666))
except OSError:
    # close on any error
    print("can't open the connection")
    sys.exit(1)

# say hello to the server
message = b'NICK irc_scribble_bot\r\nUSER irc_scribble_bot 0 * :test bot\r\n'
if len(message) != connection.send(message):
    print("an error occured")

# reading server response
serverbytes = connection.recv(4096)
## receive data/read into bytearray until bot is accepted
while(b':irc_scribble_bot MODE irc_scribble_bot :+i' not in serverbytes):
    serverbytes = connection.recv(4096)
print(serverbytes)

# close the connection
connection.close()
