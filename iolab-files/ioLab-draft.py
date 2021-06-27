import os
import re 

# ioLab.py v0.9
# 
# DANTE AVIÑÓ - 106390
# 
 
# STEP 1: Read the following instructions carefully.
 
# You will provide your solution to the IO Lab by
# editing the collection of functions in this source file.

# For input/output, you only can use os.read() and os.write() functions. 
# However, you can use print()  in the showXXX functions  and for debugging purposes.

# This is an example!
# Argument filename is a path to the fastq file to read
# This function opens filename and reads the header and the sequence of bases and prints the last on screen
def showSequence(filename):
    fd  = os.open(filename, os.O_RDONLY)
    headerline = readLine(fd)      
    seqline    = readLine(fd)
    writeLine(b''.join(seqline))
    fd.close()
    return 0


# str is a vector of ASCII bytes representing digits from 0 - 9
# function atoi converts str to integer.  The behavior is must be the same as 
# int(b''.join(str))
# example: if str = [b'3',b'0',b'9'] then  atoi(str) =  309
def atoi(str):
    out = 0
    for a in str:
        out = (int(a) + out) * 10   
    return (out//10)


# line is a byte string ended by '\n'
# that contains "length=<nnn>", where <nnn> are ascii digits
# readLenght(line) must return an integer
def readLength(line):    
    regex = r'length=(\d+)'
    matches = re.findall(regex,line)    
    return atoi(matches)


# Argument fd is a file descriptor of an already open file
# This functions returns a list of bytes read from the file 
# until a new line is reached (b'\n')
def readLine(fd):
    out = fd.readline()
    return out


# Argument line is a Fastq line in a bytestring. 
# like the return of readLine(fd).
# This function writes all the line to standard output
def writeLine(line):
    print(line)
    return 0


# Argument filename is a path to the fastq file to  read
# This function opens filename and reads its first line, printing on screen
# the name of the sequence and the number of bases
def showHeader(filename):
    fq = open(filename,"rt" )
    line = readLine(fq)
    regex = r'(\@.*) length=(\d+)'
    matches = re.findall(regex,line)    
    print("Name: %s, Number of Bases: %s" % (matches[0][0],matches[0][1]))
    fq.close()
    return


# Argument filename is a path to the fastq file to read
# This function opens filename and reads bases on its fisrt sequence. For each base, 
# prints a pair base --> quality
def showSeqQlty(filename):
    fq = open(filename,"rt" )
    while True:
        headerline = readLine(fq)
        if headerline:
            seqline    = readLine(fq)
            breakline  = readLine(fq)
            qltyline   = readLine(fq)
            seqlength = readLength(headerline)
            for i in range(seqlength):
                print ("%c --> %d" % (seqline[i], ord(qltyline[i])-33 ), end ='\n')
        else:
            break    
    return 0


# Arguments are bytestrings sequence of bases and its correspondence qualities
# The function returns de worst pair, ie, the base with the lowest quality
# Returns a list [base, quality] of the worst pair base -> quality
def worstQlty(seqLine, qltyLine): 
    worstqlty =  ord( qltyLine[0] ) - 33 
    base      = seqLine[0]
    seqlength = len( seqLine )

    for i in range(seqlength):
        quality =  ord( qltyLine[i] ) - 33 
        if ( quality < worstqlty ):
            worstqlty = quality
            base = seqLine[i]

    return [base,worstqlty]

# Argument filename is a path to the fastq file to read
# This function opens filename and reads its bases. 
# It shows the worst pair. 
# Prints a pair base --> quality
def showWorstQlty(filename):
    fq = open(filename,"rt" )
    # Read first sequence
    headerline = fq.readline().rstrip("\n")    
    if headerline:                
        seqline   = fq.readline().rstrip("\n")
        breakline = fq.readline().rstrip("\n")
        qltyline  = fq.readline().rstrip("\n")
        allworst = worstQlty(seqline,qltyline)

    while True:
        headerline = fq.readline().rstrip("\n")
        if headerline:            
            seqline   = fq.readline().rstrip("\n")
            breakline = fq.readline().rstrip("\n")
            qltyline  = fq.readline().rstrip("\n")
            worst = worstQlty(seqline,qltyline)

        if (worst[1] < allworst[1]):
            allworst = worst
        else:
            break
    print("The worst: %c -> %d" % (allworst[0],allworst[1]))    
    return 0

    

filename = 'SRR000049.fastq'
scriptdir = os.path.dirname(__file__)
filepath = os.path.join(scriptdir,filename)
#showHeader(filepath)
showSequence(filepath)
#showSeqQlty(filepath)
#showWorstQlty(filepath)

"""
print(atoi([b'3',b'0',b'9']))
line1 = "ACCDDFFTT lenght=453"
a = readLenght(line1)
print(a)
line2 = '@HWI-EAS209_0006_FC706VJ:5:58:5894:21141#ATCACG/1 length=453'
regex = r'(\@.*) length=(\d+)'
match = re.findall(regex,line2)    
print("%s, %s, %s" % (match[0],match[1],match[2]))
regex = r'(\@.*) length=(\d+)'
matches = re.findall(regex,line2) 
print("%s, %s, %s" % (matches[0],matches[1],matches[2]))
filename = 'SRR.fastq'
filename = 'SRR000033.fastq'
scriptdir = os.path.dirname(__file__)
filepath = os.path.join(scriptdir,filename)
filepath = 'C:\cit\SRR.fastq'
fq = os.open(filepath, os.O_RDONLY)
fq = open(filepath, "rt")
line = readLine(fq)
regex = r'(\@.*) length=(\d+)'
matches = re.findall(regex,line) 
print (matches[0][0])
print (matches[0][1])
#print(f"Name: {matches[0][0]}, Number of Bases: {matches[0][1]}"  )
print("Name: %s, Number of Bases: %s" % (matches[0][0],matches[0][1]) )
print("Name: %s, Number of Bases: %d" % (matches[0][0],atoi(matches[0][1])) )
"""



