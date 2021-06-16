#!/usr/bin/python3 -s
# Reads from standard input and writes to the standard output, byte by byte.
import os
import sys
c=os.read(0,1)
while (len(c)>0):
    os.write(1,c)
    c=os.read(0,1)
