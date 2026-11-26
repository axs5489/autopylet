#!/usr/bin/env python
from __future__ import print_function, unicode_literals
##############################################################################
# Text comparison utility                                                    #
##############################################################################
__author__  = 'Arshia Sasson'                                                #
__date__    = '25-Nov-2026'                                                  #
__version__ = '0.1.0'                                                        #
##############################################################################
#   DATE   | VERSION |  AUTHOR  | CHANGELOG                                  #
#----------|---------|----------|--------------------------------------------#
# 20-07-10 |  0.0.1  | asasson  | Initial draft                              #
# 26-11-10 |  0.1.0  | asasson  | Modernization (tabs, header)               #
##############################################################################
#                             See LICENSE at the base directory              #
##############################################################################
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from idlelib.redirector import WidgetRedirector

def compareline(line1, line2, orderedcmp = True):
    score = 100
    indexA, indexB = [], []
    for i1, line1 in enumerate(line1.strip()):
        s1 = line1
        print(s1)
        for i2, line2 in enumerate(line2.strip()):
            s2 = line2
    return score

def comparestr(str1, str2, orderedcmp = True):
    indexA, indexB = [], []
    for i1, line1 in enumerate(str1.split('\n')):
        s1 = line1
        print(s1)
        for i2, line2 in enumerate(str2.split('\n')):
            s2 = line2
            # matching line1 from both files
            if s1 == s2:
                # print IDENTICAL if similar
                print("Line ", i1, ": IDENTICAL")
                indexA[i1] = i2
                indexB[i2] = i1
                
            else:
                print("Line ", i1, ":")
                # else print that line from both files
                print("\tFile 1:", line1, end='')
                print("\tFile 2:", line2, end='')
            break

def comparefiles(path1, path2, orderedcmp = True):

    with open(path1, "r") as f1, open(path2, "r") as f2:
        return comparestr(f1, f2, orderedcmp)
        

class ReadOnlyScrolledText(ScrolledText):
    def __init__(self, master=None, **kwargs):
        ScrolledText.__init__(self, master, **kwargs)
        self.redirector = WidgetRedirector(self)
        self.insert = self.redirector.register("insert", lambda *args, **kw: "break")
        self.delete = self.redirector.register("delete", lambda *args, **kw: "break")
        
if __name__ == "__main__":
    f1 = "C:\\Users\\asasson\\Documents\\Logs\\2313_RED.txt"
    f2 = "C:\\Users\\asasson\\Documents\\Logs\\2313_BLK.txt"
    s1, s2 = "", ""
    
    with open(f1, "r") as f1, open(f2, "r") as f2:
        for line in f1:
            s1 += line
        for line in f2:
            s2 += line
