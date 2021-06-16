#!/usr/bin/env python3
# seqFastqParser.py version 0.1
# Last modified on Fri 28 May 2021
import sys
import os
import signal
import struct
import ioLab as io


try:
    fn = sys.argv[1]
except IndexError as ie:
    print("Usage:",sys.argv[0], "fasq filename")
    sys.exit(1)

if not os.path.exists(fn):
    print("Error: File does not exist\n")
    sys.exit(2)

 
print("File: ",fn, "Fastq header")
io.showHeader(fn)
print("File: ",fn, "First sequence")
io.showSequence(fn)
print("File: ",fn, "First sequence and qualities")
io.showSeqQlty(fn)
print("\nFile: ", fn, "The worst quality of the first sequence")
io.showWorstQlty(fn)




