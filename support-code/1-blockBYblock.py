#!/usr/bin/python3 -s
import os
import sys
SIZE=128
c=os.read(0,SIZE)
while (len(c)>0):
    os.write(1,c)
    c=os.read(0,SIZE)