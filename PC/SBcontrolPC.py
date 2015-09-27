#!/usr/bin/env python
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
# Echo server program
import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 12998              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr
while 1:
    serialCmd = raw_input(">>>") # Send the data:
    conn.sendall(serialCmd)
    
    #if not data: break # Read back
    data = conn.recv(4096)
    print(data)
conn.close()
