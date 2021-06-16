#!/usr/bin/env python
import os
import sys
#8-base-counters_shared
#Counts how many bases A and G are in a FASTQ file


def counter (base):
    global fd
    global ch2p
    accu = 0
    b = os.read(fd,1)
    found = False
    while (len(b)>0):
        if (b == base):
           accu +=1
        b = os.read(fd,1)
    b_accu = int.to_bytes(accu,2,byteorder='little')
    os.write(ch2p[1],b_accu)
    return accu

fd=-1
aes=0
gs=0
bases = [b'A',b'G']

try:
    fn = sys.argv[1]
except IndexError as ie:
    print("Usage:",sys.argv[0], "fasq filename")
    sys.exit(1)

if not os.path.exists(fn):
    print("Error: File does not exist\n")
    sys.exit(2)

gCounter = 0
aCounter = 0
p2ch = os.pipe()
ch2p = os.pipe()

try:
    fd  = os.open(fn, os.O_RDONLY)
except IOError as e:
   print ("I/O error ",e.errno, e.strerror)
   sys.exit(3)
except: #handle other exceptions such as attribute errors
   print("Unexpected error:", sys.exc_info()[0])
   sys.exit(4)

# skip the first line
b = os.read(fd,1)
found = False
while (len(b)>0 and not found):
    if (b == b'\n'):
        found = True
    b = os.read(fd,1)
# begin counting As and Gs
# Creating a child to count As
As = 0
Gs = 0
pid = os.fork()
if (pid == 0):
    os.close(p2ch[1]) # child writes to ch2p1] 
    os.close(ch2p[0]) # and reads from  p2ch[0]
    As = counter(bases[0])
    print (As)
    sys.exit(0)
pid = os.fork()
if (pid == 0):
    os.close(p2ch[1]) # child writes to ch2p1] 
    os.close(ch2p[0]) # and reads from  p2ch[0]
    Gs = counter(bases[1])
    print (Gs)
    sys.exit(0)

os.close(p2ch[0]) # parent writes to p2ch[1] 
os.close(ch2p[1]) # and reads from  ch2p[0]

r = int.from_bytes(os.read(ch2p[0],2), byteorder='little')
print(r)
r = int.from_bytes(os.read(ch2p[0],2), byteorder='little')
print(r)

os.close(p2ch[1])
os.close(ch2p[0])
os.wait()
os.wait()
