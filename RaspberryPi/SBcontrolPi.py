#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  SBcontrolPi.py
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

import socket, serial, time
serialNum = "/dev/ttyACM0"
HOST = ''    # The remote host
PORT = 12998 # The same port as used by the server

print("Setting up Tcp server...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print("Done. Waiting for input.")


# Find serial ports.
try:
	ser = serial.Serial(serialNum, 115200)
except:
	print "found serial port" , ser.name , "which is the default. Change it in the SBcontrolPi.py script."

# Tcp server loop.
		
while 1:
		s.send(">")
		data = s.recv(1024)
		if not data: break 
		print 'Received', repr(data)
		ser.write(repr(data))
		# Send it via Serial
		time.sleep(1)
		s.send(ser.readline(1024).decode()) # Send back output		

s.close()

