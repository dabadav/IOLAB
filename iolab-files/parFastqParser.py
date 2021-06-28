import os
import ioLab as io


# 
# parFastqParser.py v0.1
#
# DANTE AVIÑÓ - 106390
# 
 
##  ** Computes and Prints the worst quality of all the scores ** 
# 
##  In order todo that you will have two processes and two pipes.

def parser(filepath):
    # Open fasta file
    fd = os.open("SRR000049.fastq", os.O_RDONLY)

    # Creation of 2 pipes
    p2ch = os.pipe()
    ch2p = os.pipe()

    # Parent creates child process 
    pid = os.fork()

    if (pid == 0):  # Child
        # Waits reading from the pipep2ch.  
        # When the parent sends the data, child finds out the line worst quality and
        # returns to its parent a pair(base, quality) via pipe ch2p and writes the pair to an ASCII text file called worst.txt.  
        # This file is created by the child process at the beginning with permissions: rw-rw-r--.

        # Infinite loop
        while True:
            c = os.read(p2ch[0],1) # reads from the pipe ch2p
            # Compute worst
            io.worstQlty(seqline, qltyline)
            # Worst to txt
            os.write(ch2p[1],c)    # writes to the pipe ch2p

    else:
        # Loop. Each iteration, reads the length of a line, a line of sequences and and a line of qualities from the fastq file (passed as an argument 1)
        # Parent sends this information to its child, via pipep2ch
        while True:
            headerline = io.readLine(fd)
            if headerline:
                seqline   = io.readLine(fd)
                breakline = io.readLine(fd)
                qltyline  = io.readLine(fd)
                seqlength = io.readLength(headerline)
            else:
                break

        os.write(p2ch[1],c)    # writes to the pipe p2ch
        c = os.read(ch2p[0],1) # reads from the pipe ch2p

        # waits for its child returns the worst pair (base,quality), via ch2p.  
        # When there are no more lines to read,  the parent process print the worst pair to thestandard output, kills its child, clean up and ends
        
        os.write(1,c) # and writes to the stdout (terminal)
        os.wait()

filename  = 'SRR000049.fastq'
scriptdir = os.path.dirname(__file__)
filepath  = os.path.join(scriptdir,filename)


