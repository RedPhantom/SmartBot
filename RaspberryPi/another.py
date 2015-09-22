#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  SBcontrolPC.py
#
#  Copyright 2015 Itay MacBunny <itay@BoBTop>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#
import socket, select, sys

tcpAddress = "127.0.0.1" # In all cases you want to leave this address like this.
tcpConPort = 12298               # This doesn't need to be a string!
connection_list = []
backlog = 5
BUFFER_SIZE = 1024               # The buffer size. 1024 is enough.
serialCommand = ""

def main():
    #Start the Tcp server with address and port specefied as global variables.
    print("SBcontrolPC - Starting Tcp Server...")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((tcpAddress,tcpConPort))
    #s.listen(backlog)
    print("Server started on address",(s.getsockname()[0]),"(internal is 127.0.0.1) and port",tcpConPort)
    
    
    print("type EXIT in console to quit, otherwise text sent is a command to the Arduino.")
    while True:
        client, address = s.accept()
        if data:
            client.send("hello")
        client.close() 

if __name__ == '__main__':
    main()
