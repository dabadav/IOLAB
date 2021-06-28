import os,sys
from posix import O_CREAT
import ioLab as io

# parFastqParser.py v0.105
#
# DANTE AVIÑÓ - 106390
# 
 
##  ** Computes and Prints the worst quality of all the scores ** 
# 
##  In order todo that you will have two processes and two pipes.

def process1(filepath):
    # Open a fastq file given its path

    fd = os.open(filepath,os.O_RDONLY)

    # Creation of 2 pipes
    p2ch = os.pipe()
    ch2p = os.pipe()

    # Parent creates child process
    pid = os.fork()

    if (pid == 0):  # Child
        # Waits reading from the pipe p2ch.  
        # When the parent sends the data, child finds out the line worst quality and
        # returns to its parent a pair(base, quality) via pipe ch2p and writes the pair to an ASCII text file calledworst.txt.  
        # This file is created by the child process at the beginning with permissions: rw-rw-r--.
        
        fdworst = os.open('calledworst.txt', os.O_WRONLY|O_CREAT|os.O_TRUNC, 0o664)

        # Infinite loop
        while True:
            seqline  = io.readLine(p2ch[0])
            qltyline = io.readLine(p2ch[0])            
            # Compute worst
            (cbase,cworst) = io.worstQlty(seqline, qltyline)
            if (cbase):
                # Worst to txt
                os.write(ch2p[1],''.join(cbase,cworst))    # writes to the pipe ch2p
                os.write(fdworst, f"Base: {cbase}, Quality: {cworst} \n" )
            else:
                break
        os.close(ch2p[0])
        os.close(ch2p[1])
        sys.exit(0)

    # Parent process
    else: 
        # Loop. Each iteration, reads a line of sequences and a line of qualities from the fastq file (passed as an argument 1)
        # Parent sends this information to its child, via pipep2ch (using io.writeLine and stdout redirection)
        
        # Redirect standard output to the p2ch write pipe, i.e. p2ch[1]
        #old_stdout = sys.stdout
        #sys.stdout = p2ch[1]
        
        while True:
            headerline = io.readLine(fd)
            worst = b'\xff'  # higher possible quality 
            if headerline:                
                seqline   = b''.join(io.readLine(fd))
                io.readLine(fd) # breakline
                qltyline  = b''.join(io.readLine(fd))
                # It writes to the p2ch pipe, because of stdout redirection
                io.writeLine2(p2ch[1],seqline)
                io.writeLine2(p2ch[1],qltyline)
                # Waits to read the worst quality pair (base,quality) from  child project
                (seqbase,seqquality) = os.read(ch2p[0],2)                
                if (seqquality < worst):
                    (base,worst) = (seqbase,seqquality)
            else:
                break
        
        # waits for its child returns the worst pair (base,quality),viach2p.  
        # When there are no more lines to read,  the parent process print the worst pair to thestandard output, kills its child, clean up and ends
        
        sys.stdout = old_stdout
        print ("Base: %c -> Quality: %d" % (base,io.atoi(worst)-33) )
        os.close(p2ch[0])
        os.close(p2ch[1])
        os.wait()


filename  = 'SRR000049.fastq'
scriptdir = os.path.dirname(__file__)
filepath  = os.path.join(scriptdir,filename)
process1(filepath)
