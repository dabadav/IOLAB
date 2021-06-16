#!/usr/bin/python3 -s
# lswc.py
# ls | wc
import os
import sys

fd =  os.pipe()
pid =  os.fork()

if ( pid == 0):
    os.close(fd[0])
    os.close(1)
    os.dup(fd[1])
    os.close(fd[1])
    os.set_inheritable(1, True)
    os.execlp("ls","ls")
    sys.exit(1)
else:
    pid = os.fork()
    if (pid == 0):
        os.close(fd[1])
        os.close(0)
        os.dup(fd[0])
        os.close(fd[0])
        os.set_inheritable(0, True)
        os.execlp("wc","wc")
        sys.exit(2)
    else:
        os.close(fd[0])
        os.close(fd[1])
        os.wait()
        os.wait()


