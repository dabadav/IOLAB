import os
import re 


# ioLab.py version 0.1
# Last modified on Fri 28 May 2021
# This module contains all the functions you must program. 
# 
# Instructions to Students:
 
# STEP 1: Read the following instructions carefully.
 
# You will provide your solution to the IO Lab by
# editing the collection of functions in this source file.

# For input/output, you only can use os.read() and os.write() functions. 
# However, you can use print()  in the showXXX functions  and for debugging purposes.

# This is an example!
# Argument filename is a path to the fastq file to read
# This function opens filename and reads the header and the sequence of bases and prints the last on screen
def showSequence(filename):
    fd  = open(filename, "rt")
    # The first line is just read and not used
    line = readLine(fd)  
    # The seconbd line contains the actual sequence
    line = readLine(fd)
    writeLine(b''.join(line))
    os.write(1,b'\n')
    os.close(fd)
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

def new_func():
    return 0

# Argument filename is a path to the fastq file to  read
# This function opens filename and reads its bases. For each base, 
# prints a pair base --> quality
def showSeqQlty(filename):

    return 0


# Arguments are bytestrings sequence of bases and its correspondence qualities
# The function returns de worst pair, ie, the base with the lowest quality
# Returns a list [base, quality] of the worst pair base -> quality
def worstQlty(seqLine, qltyLine):
 
    return []

# Argument filename is a path to the fastq file to  read
# This function opens filename and reads its bases. 
# It shows the worst pair. 
# Prints a pair base --> quality
def showWorstQlty(filename):
   
    return 0

filename = 'SRR.fastq'
filepath = 'C:\cit\SRR.fastq'

showHeader(filepath)
showSequence(filepath)

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



