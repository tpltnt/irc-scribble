#!/usr/bin/env python3

"""
A very basic script to leave messages for others in an IRC channel.

:author: tpltnt
:license: AGPLv3 (or later)
"""

import socket
import sys

botname = "irc_testbot"
channel = "#ircscribble"


# open a socket to talk to a freenode IRC server (in clear text)
try:
    # IRC is TCP, so the python defaults are fine
    connection = socket.create_connection(("chat.freenode.net", 6666))
except OSError:
    # close on any error
    print("can't open the connection")
    sys.exit(1)

# say hello to the server -> client bytes
cbytes = b'NICK ' + bytes(botname, 'ascii') + b'\r\nUSER ' + bytes(botname, 'ascii') + b' 0 * :test bot\r\n'
if len(cbytes) != connection.send(cbytes):
    print("an error occured")

# reading server response
serverbytes = connection.recv(4096)
## receive data/read into bytearray until bot is accepted
while((b'MODE ' + bytes(botname, 'ascii') + b' :+i') not in serverbytes):
    serverbytes = connection.recv(4096)
    if b':Nickname is already in use.' in serverbytes:
        print("nick already in use")
        sys.exit(2)
#print(serverbytes)


# join a channel
cbytes = b'JOIN ' + bytes(channel, 'ascii') + b'\r\n'
if len(cbytes) != connection.send(cbytes):
    print("an error occured")
serverbytes = connection.recv(4096)
clientstring = ''
if b'JOIN' in serverbytes:
    clientstring = str(serverbytes).split(' ')[0]
    clientstring = clientstring.split('!')[1]
#
# do you magic bot action here
#
cbytes = b'PRIVMSG ' + bytes(channel, 'ascii') +  b' :i am a bot, nothing special\r\n'
if len(cbytes) != connection.send(cbytes):
    print("an error occured")
serverbytes = connection.recv(4096)
## receive data/read into bytearray until bot is accepted
while((b'go away') not in serverbytes):
    # handle PING-PONG
    if b'PING' in serverbytes:
        cbytes = b'PONG :' + bytes(clientstring, 'ascii') +  b'\r\n'
        if len(cbytes) != connection.send(cbytes):
            print("an error occured during PING-PONG")
    print(serverbytes)
    serverbytes = connection.recv(4096)

print(serverbytes)

# leave the channel
cbytes = b'QUIT :Gone to data heaven\r\n'
if len(cbytes) != connection.send(cbytes):
    print("an error occured")
print(connection.recv(4096))

# close the connection
connection.close()
