#!/usr/bin/python3 -s
# rnd-access.py
# reads positions multiples of 4
import os

fd =  os.open("Helian.fasta",os.O_RDONLY)
c = os.read(fd,1)
while (len(c)>0):
    os.write(1,c)
    os.lseek(fd,4, os.SEEK_CUR)
    c = os.read(fd,1)
