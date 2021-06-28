##### -------------------------------------------------------- #####
##### ------------ Dante Aviñó, Oriol Castellano ------------- #####
##### ----------------------   PROCLAB   --------------------- #####
##### -------------------------------------------------------- #####


#### Importing modules proclab
import os
import sys
import time
import signal


#### FUNCTIONS

# Creates n processes. All of them execute the f function
# Returns the number of created children 
# Syscalls needed: os.fork
# If an error occurs, raise the exception 
def createChildren(n,f):
    out = 0

    for _ in range(n):
        p = os.fork()
        if p > 0:
            out += 1      # Count created process
        elif p == 0:
            f(p)
        else:
            raise Exception("Exception: error.")

    return out


# Argument status is a list, the return of os.wait()
# Returns a list of two numbers and a string: 
# the child's pid, 
# the child's exit value or signumber 
# the  cause of child's termination. "exit" or "signal"
# Syscalls allowed: none
# Functions needed: os.WTERMSIG(...), os.WEXITSTATUS(...), os.WTERMSIG(...)
def check_status(status): 
    out = list()
    out.append(status[0])

    if os.WIFEXITED(status[1]):
        x = "Termination: EXIT"      # Termination by exit
        n = os.WEXITSTATUS(status[1])
    else:
        x = "Termination: SIGNAL"    # Termination by signal
        n = os.WTERMSIG(status[1])

    out.append(n)
    out.append(x)

    return out


# Waits for n children
# Returns a list of tuplas with the pid and 
# the exit value or signal number of the n dead children
# Syscalls needed: os.wait
# If an error occurs, raise the exception
def waitNChildren(n):
    out = list()

    for _ in range(n):
        out.append(os.wait())

    return(out)


# Waits for all already dead children
# Returns a list of tuplas with the status list returned by the syscall
# Syscalls needed: os.waitpid
def waitChildren():
    while True:
        out = list()
        s = os.waitpid(-1, os.WNOHANG)

        if s != (0,0):
            out.append(s)
            return out
        
        elif s[0] == -1:
            break


# Sends signal s to process p
# Returns 0 on success
# Syscalls needed: os.kill
# If an error occurs, raise the exception
def sendSignal(p,s):
    try:
        os.kill(p,s)
        return 0

    except:
        raise Exception("Exception: signal error")


# Set the handler for signal signalnum to the function handler
# On sucess returns the previous signal handler 
# Syscalls needed: signal.signal
# If an error occurs, raise the exception and returns -1
def sigAction(s,f):
    try:
        signal.signal(s,f)
        return f

    except:
        raise Exception("Exception: error")


# replaces the current process image with a new process image
# path is the complete file name of a executable, 
# args, is a list of the arguments of path
# Syscalls needed: os.execlp
# If an error occurs, raise the exception
def chgProcImg(path,args):
    try:
        os.execlp(path, args[0], args[1], args[2])

    except:
        raise Exception("Exception: error")


# Creates a process and replaces the child process image with program named f
# Second parameter, a, is a list of the arguments of f
# Returns the pid of the child
# Syscalls needed: os.fork, os.execvp
# If an error occurs, raise the exception 
def launchCmd(f,a):
    args = [f] + [a]
    out = os.fork()

    if out == 0:
        os.execvp(f, args)

    return(out)
