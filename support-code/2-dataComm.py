#!/usr/bin/python3 -s
import os
import sys

def func_p1(fdin, fdout):
    buff = os.read(fdin,16)
    os.write(fdout,buff)
    return 0
def func_p2(fdin, fdout):
    buff = b'Hello world\n'
    os.write(fdout,buff)
    buff = os.read(fdin,16)
    os.write(1,buff)
    return 0
pipe1 = os.pipe()
pipe2 = os.pipe()
pidp1 = os.fork()
if (pidp1==0):
    os.close(pipe1[0])
    os.close(pipe2[1])
    func_p1(pipe2[0],pipe1[1])
    sys.exit(0)
os.close(pipe1[1])
os.close(pipe2[0])
pidp2 = os.fork()
if (pidp2 == 0):
    func_p2(pipe1[0],pipe2[1])
    sys.exit(0)
os.close(pipe1[0])
os.close(pipe2[1])
os.wait()
os.wait()
