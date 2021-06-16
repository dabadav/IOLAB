#!/usr/bin/python3 -s
# parent and child communicating via pipe
import os
import sys

fd = os.pipe()
pid =  os.fork()
if ( pid == 0):                 # child process
    os.close(fd[0])
    c = os.read(0,1)            # reads from stdin 
    while (len(c)>0):
        os.write(fd[1],c)        # and writes to the pipe
        c = os.read(0,1)        
else:                           # parent process
    os.close(fd[1])
    c = os.read(fd[0],1)       # reads from the pipe
    while (len(c)>0):
        os.write(1,c)           # and writes to the stdout
        c = os.read(fd[0],1)
    os.wait()
