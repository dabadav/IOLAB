#!/usr/bin/python3 -s
# cat < file1.txt > file2.txt
import os


os.close(0)
fd1 = os.open ("file1.txt", os.O_RDONLY)
os.close(1)
fd2 = os.open ("file2.txt", os.O_WRONLY|os.O_CREAT|os.O_TRUNC,0b110110110)
os.set_inheritable(1,True)
os.set_inheritable(0,True)
os.execlp("cat","cat")

