import os
import ioLab as io

##  ** Computes and Prints the worst quality of all the scores ** 
# 
##  In order todo that you will have two processes and two pipes.

# Open fasta file
fd= os.open("SRR000049.fastq",os.O_RDONLY)

# Creation of 2 pipes
p2ch = os.pipe()
ch2p = os.pipe()

# Parent creates child 'pq' process
pid = os.fork()

if (pid == 0):  # Child
    # Infinite loop
    while True:
        c = os.read(p2ch[0],1) # reads from the pipe ch2p
        # Compute worst
        io.showWorstQlty(filename)
        # Worst to txt
        os.write(ch2p[1],c)    # writes to the pipe ch2p

else:
    # Loop. Each iteration, reads the length of a line, a line of sequences and and a line of qualities from the fastq file (passed as an argument 1)
    # Parent sends this information to its child, via pipep2ch
    for i in range(len):
        os.write(p2ch[1],c)    # writes to the pipe p2ch
        c = os.read(ch2p[0],1) # reads from the pipe ch2p
        read fastq
    os.write(1,c) # and writesto the stdout (terminal)
    os.wait()

