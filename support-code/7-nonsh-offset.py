
#!/usr/bin/python3 -s
# nonsh-offset.py
# counts number of A in sequential, non sharing the fd
import os

nAs = 0
pid =  os.fork()
fd = os.open("Helian.fasta",os.O_RDONLY)
c = os.read(fd,1)
while (len(c)>0):
    if (c == b'A'):
         nAs +=1
    c = os.read(fd,1)
print ("Number of A:",nAs)
os.close(fd)
