#!/usr/bin/python3 -s
# fsz.py
# computes the file size of "Helian.fasta"
import os
fd = os.open("Helian.fasta",os.O_RDONLY)
sz = os.lseek(fd,0, os.SEEK_END)
print (sz)
