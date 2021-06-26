# IOLAB
Understand how I / O system calls work. Deal with bytes, how to interpret (str, int, ...)

Input files: FASTQ format 

--> Read & Interpret 

--> Syncronize 2 processes to read and compute quality errors concurrently.

------

SYSTEM CALLS: open, read, write, close and pipe

<u>HANDOUT</u>: **ioLab.py**; **parFastqParser.py** must be edited and delivered.

**ioLab.py**

- toi(str) Converts the bytestring str to integer 2
- readLine(fd) Returns a line, in a list of bytes, read from the file descriptor fd. 1
- writeLine(line) Prints line to standard output. 1
- readLenght(line) Returns the lenght of a sequence. 2
- showHeader(filename) Prints name and length of a Fastq file. 1
- showSeqQlty(filename) Prints pair base-¿quality. 2
- worstQlty(seqLine, qltyLine) Returns the worst pairs base→quality. 3
- showWorstQlty(filename) Prints the worst pair base→quality. 1

**parFastqParser.py**
Computes and prints the worst quality of all the scores. 
In order to do that you will have two processes and two pipes. 

- One pipe, named p2ch (from parent to child) where the parent writes and the child reads. 
- Other one, named ch2p (from child to parent), where the child writes and the parent reads. 

The parent process executes a loop. Each iteration, it reads the length of a line, a line of sequences and and a line of qualities from the fastq file (passed as an argument 1 to the program).
Parent sends this information to its child, via pipe p2ch, and waits for its child returns the worst pair (base, quality),via ch2p. When there are no more lines to read, the parent process print the worst pair to the standard output, kills its child, clean up and ends.
The child process executes an infinite loop. Its waits reading from the pipe p2ch. When the parent sends the appropriate information, the child finds out the worst quality of the line and returns to its parent a pair (base, quality) via pipe ch2p and writes the pair to an ASCII text file called worst.txt. 
This file is created by the child process at the beginning with permissions: rw-rw-r--.

------

FASTQ is a text-based format for storing both nucleotide sequence and its corresponding quality score. 

It has 4 lines per sequence:
• @ the unique sequence name.
• The nucleotide sequence (A, C, G, T, N) on 1 line.
• + The quality line break. Sometimes with the sequence name again.
• The quality scores (ASCII characters) on 1 line.

```
@HWI-EAS209_0006_FC706VJ:5:58:5894:21141#ATCACG/1
TTAATTGGTAAATAAATCTCCTAATAGCTTAGATNTTACC
+HWI-EAS209_0006_FC706VJ:5:58:5894:21141#ATCACG/1
efcfffffcfeefffcffffffddf‘feed]‘]_Ba_ˆ__
```

Phred Quality Scores (Q-Score) in FASTQ files represent the probability of error of each base in the se-
quence field. A Q-Score of 40 represents a probability of error of 0.00010, while a Q-Score of 0 represents
a probability of error of 1.00000. 

Represented as an ASCII character from the following table, in which the ASCII code to represent a Q-Score q is calculated as: chr(q + 33). Therefore, a Q-Score of 0 would be represented by the ASCII character in position 33 (‘!’), while a Q-Score of 80, would be represented by the character in position 113 (‘q’).

------

Support code:

0-byteBYbyte.py
Reads from standard input and writes to the standard output, byte by byte.

1-blockBYblock.py
Reads from standard input and writes to the standard output, block by block.

2-DataComm.py
Main process creates two more processes that communicate each other via two pipes.

3-rnd-access.py
Reads positions multiples of 4 from the file “Helian.fasta”

4-fsz.py
Computes the file size of "Helian.fasta"

5-pipe-basic.py
Parent and child communicating via pipe

6-sh-offset.py
Counts number of A in parallel, sharing the fd

7-nonsh-offset.py
Counts number of A in sequential, non sharing the fd

8-base-counters_shared.py
Counts how many bases A and G are in a FASTQ file
It does not work properly because it’s sharing the file descriptor

9-base-counters.py
Counts how many bases A and G are in a FASTQ file
It works ok.

10-redit.py
Simulates the command-line 
$ cat < file1.txt > file2.txt

11-lswc.py
Simulates the command-line 
$ ls | wc
