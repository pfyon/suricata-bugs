#!/usr/bin/env python3

import sys
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((sys.argv[1], int(sys.argv[2])))

s.sendall(b'\x00\x00\x00\x00')
s.sendall(b'\x01\x02\x03\x04\x05\x06\x07\x08')
s.close()
