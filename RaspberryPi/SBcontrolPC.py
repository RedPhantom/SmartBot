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
import socket

tcpAddress = "127.0.0.1" # In all cases you want to leave this address like this.
tcpConPort = 12298		 # This doesn't need to be a string!

BUFFER_SIZE = 1024		 # The buffer size. 1024 is enough.
serialCommand = ""


def main():
	#Start the Tcp server with address and port specefied as global variables.
	print("SBcontrolPC - Starting Tcp Server...")
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((tcpAddress, tcpConPort))
	s.listen(3)
	
	print("Server started on address",(s.getsockname()[0]),"(internal is 127.0.0.1) and port",tcpConPort)
	print("type EXIT in console to quit")
	
	while 1:
		serialCommand = input(">>>")
		if (serialCommand == "EXIT"):
			s.close()
			return 0
		try:
			s.send(serialCommand.encode()) # We encode it to allow transmission via bytes.
		except:
			print("error. It is possible that the client wasn't listening")	
	return 0

if __name__ == '__main__':
	main()

