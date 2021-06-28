#!/usr/bin/env python
# TIACOS proclab
# version 0.3
# Licensed by upccommons

import proclab as pl
import sys
import getopt
import signal
import os
import time

selfpid = os.getpid()
n = 3
passed = "NOT passed"

def timeout(signum, frame):
    global passed
    global n
    passed = "NOT passed"
    n = 0

def usrHandler(signum, frame):
    global passed 
    passed = "passed"

def noisy_mode():
    os.dup2(5,1)
    os.dup2(5,2)

def quite_mode():
    os.dup2(1,5)
    os.close(1)
    os.open("/dev/null",os.O_RDWR)
    os.close(2)
    os.dup(1)
 

def childHandler(signum, frame):
    global n
    global passed
    l = pl.waitChildren()
    if n == len(l):
        passed = "passed"
    n-=len(l)

def myFunc(i):
    os._exit(i)

def usage():
    print("Usage: ", sys.argv[0], "-n <number of processes>")
    sys.exit(1) 

def test_waitNChildren(children):
    global passed
    r = list()
    passed = "NOT passed"    
    print("*** [001] calling waitNChildren(n)    ", end="",flush=True)
    try:
        r = pl.waitNChildren(children)
    except:
         print("OS error: {0}".format(OSError))
         sys.exit(1)
    else:
        if len(r) == children:
            passed = "passed"
        print("\t\t", passed,"***")
    return r

def test_createChildren(children, legacy = False ):
    global passed
    passed = "NOT passed"
    if not legacy:
        print("*** [000] calling createChildren(n,f)", end="",flush=True)
    try:
        ndChld = pl.createChildren(children,myFunc)
    except OSError:
         print("OS error: {0}".format(OSError))
         sys.exit(1)
    else:
        if   ndChld == children:
            passed = "passed"
        print ("\t\t", passed, "***")
    if not legacy:
        cmd = "killall " + sys.argv[0] + " 2> /dev/null"
        os.system(cmd)

def test_checkStatus(n):
    global passed
    passed = "NOT passed"
    print("*** [010] calling check_status(status)", end="",flush=True)
    s = pl.check_status([os.getpid(),n])
    if len(s) > 0 and s[0]>=0 and s[1]>=0:
        passed = "passed"
    print("\t\t", passed, "***")

def test_launchCmd():
    global passed
    passed = "NOT passed"
    print("*** [011] calling launchCmd(f,a) ***",flush=True)
    quite_mode()
    pid = pl.launchCmd("uname","-r")
    noisy_mode()
    if pid > 0:
        passed = "passed"
    print("\n\t\t\t\t\t\t", passed, "***")

def test_sendSignal():
    print("*** [100] calling sendSignal(p,s) ***", end="",flush=True)
    pl.sigAction(signal.SIGUSR1,usrHandler)
    pl.sendSignal(os.getpid(),signal.SIGUSR1)
    print("\t\t", passed,  "***")

def test_waitChildren():
    passed = "NOT passed"
    print("*** [101] calling waitChildren() ***", end="",flush=True)
    
    r=os.fork()
    if r>0:
        r=os.fork()
        if r>0:
            r=os.fork()
            if r>0:
                time.sleep(1)
                lwaits = pl.waitChildren()
                if (len(lwaits)==3):
                    passed = "passed"
                    for stat in lwaits:
                        if stat[0]==0:
                            passed = "NOT passed"
                            break
                print("\t\t", passed, "***")
                return r 
    os._exit(0)

def test_chgProcImg():
    passed = "NOT passed"
    print("*** [110] calling chgProcImg(path,args). \n \t If passed, no return ***")
    path = "/bin/ls"
    args = ["-l","-a","-i"]
    #quite_mode()
    pl.chgProcImg(path,args)
    #noisy_mode()
    print("\n\t\t\t\t\t\t", passed, "***")


def main():
    global passed
    signal.signal(signal.SIGALRM,timeout)
    try:
        if len(sys.argv) < 2:
            usage()
        optlist, opt = getopt.getopt(sys.argv[1:],'n:')
    except getopt.GetoptError as err:
        print (err)
        usage()
    else:
        if optlist[0][0] == "-n":
            try:
                N = int(optlist[0][1])
            except:
                print("n is not a number")
                usage()
   
    print("Testing proclab. Version 0.2, last modified on Sat 25 May 17:39")
    test_createChildren(N)
    test_waitNChildren(N)
    test_checkStatus(0xff00)
    test_launchCmd()
    test_sendSignal()
    test_waitChildren()
    test_chgProcImg() 
    
   



if __name__ == "__main__":
    main()
