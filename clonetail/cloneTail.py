#!/usr/bin/python

import sys
from optparse import OptionParser


def countLine(filename):
    cnt = 0
    with open(filename) as f:
        for line in f:
            cnt += 1
    return cnt



def getLastLineFromHandler(h, n):
    bufferLine = []
    for line in h:
        if (len(bufferLine) >= n):
            bufferLine.pop(0)
        bufferLine.append(line)
    print "".join(bufferLine),   



def getLastLines(options, args):
    n = options.n

    if (len(args) == 0):
        getLastLineFromHandler(sys.stdin, n)
    else:
        multi_file = len(args) > 1
        for fn in args:
            try:
                h = open(fn, "r")
                if (multi_file and not options.q): print "==> %s <==" % (fn)
                getLastLineFromHandler(h, n)
                h.close()
            except Exception, e:
                print "cloneTail: %s " %str(e)

def getLastCharFromHandler(h, n):
    bufferChar = ""
    for line in h:
        bufferChar += line
        if (len(bufferChar) > n):
            bufferChar = bufferChar[-n:]
    print bufferChar,  


def getLastChars(options, args):
    n = options.c
    if (len(args) == 0):
        getLastCharFromHandler(sys.stdin, n)
    else:
        multi_file = len(args) > 1
        for fn in args:
            try:
                h = open(fn, "r")
                if (multi_file and not options.q): print "==> %s <==" % (fn)
                getLastCharFromHandler(h, n)
                h.close()
            except Exception, e:
                print "cloneTail: %s " %str(e)


def tail(fname, outLine):
    lines = [""] * outLine
    i = 0
    for line in reversed(open(fname).readlines()):
        if i < outLine:
            lines[outLine -1 -i] = line.rstrip()
            i += 1
        else: break
    for x in lines:
        print x

usage = "tail - output the last part of files\nusage: %prog  [-q] [-b # | -c # | -n #] [file ...]"

parser = OptionParser(usage=usage)

parser.add_option("-q", "--quiet", action="store_true",
                  help = " never output headers giving file names",
                  dest = "q")

parser.add_option("-n", "--line", type = "int",
                  help = " get tail lines from File",
                  dest = "n")
parser.add_option("-b", "--block", type = "int",
                  help = " get tail block from File",
                  dest = "b")
parser.add_option("-c", "--bytes", type = "int",
                  help = "output the last K bytes; or use -c +K to output bytes starting with the Kth of each file", 
                  dest = "c")

   
              
options, args = parser.parse_args()

if (options.n == None  and options.b == None and options.c == None):
    options.n = 10

if (options.b != None and options.n != None):
    parser.print_help()
    exit(-1)

if (options.n != None) :
    getLastLines(options, args)
if (options.c != None) :
    getLastChars(options, args)
if (options.b != None) :
    options.c = options.b * 512
    getLastChars(options, args)
 