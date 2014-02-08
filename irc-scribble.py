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
    connection = socket.create_connection(("chat.freenode.net", 6666))
except OSError:
    # close on any error
    print("can't open the connection")
    sys.exit(1)

# close the connection
connection.close()
