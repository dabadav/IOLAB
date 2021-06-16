#!/usr/bin/python3 -s
#sh-offset.py
# counts number of A in parallel, sharing the fd
import os


fd = os.open("Helian.fasta",os.O_RDONLY)
nAs = 0
pid =  os.fork()
c = os.read(fd,1)
while (len(c)>0):
    if (c == b'A'):
         nAs +=1
    c = os.read(fd,1)
print ("Number of A:",nAs)
os.close(fd)
