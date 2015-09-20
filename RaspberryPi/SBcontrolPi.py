#!/usr/bin/env python3
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
import socket

tcpAddress = "127.0.0.1" # In all cases you want to leave this address like this.
tcpConPort = 12298		 # This doesn't need to be a string!

BUFFER_SIZE = 1024		 # The buffer size. 1024 is enough.

def main():
	#Start the Tcp server with address and port specefied as global variables.
	print("SBcontrolPi - Starting Tcp Client...")
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((tcpAddress, tcpConPort))
	s.listen(3)
	
	print("Client started on address",tcpAddress,"and port",tcpConPort)
	print("type EXIT in console to quit")
	
	while 1:
		try:
			data = s.recv(BUFFER_SIZE)
		except:
			print("Error 107. Could not connect: is the server down? Is the client connected to the LAN?")
		print(data)
		time.sleep(0.5)
if __name__ == '__main__':
	main()

