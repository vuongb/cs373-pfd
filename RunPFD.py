#!/usr/bin/env python

# ------------------------------
# projects/collatz/RunPFD.py
# Copyright (C) 2012
# Michael Tarng & Bryan Vuong
# -------------------------------

"""
To run the program
    % python RunCollatz.py < RunPFD.in > RunPFD.out
    % chmod ugo+x RunCollatz.py
    % RunPFD.py < RunPFD.in > RunPFD.out

To document the program
    % pydoc -w PFD
"""

# -------
# imports
# -------

import sys 
import StringIO
from PFD import pfd_solve

# ----
# main
# ----
a = sys.stdin
stringArray = []
arrayArray = []
s = ""
counter = 1
for line in sys.stdin :
    if line.rstrip() :
        stringArray.append(line)
    else :
        arrayArray.append(stringArray)
#        for i in stringArray:
#            s += i
#        pfd_solve(StringIO.StringIO(s), sys.stdout)
#        s = ""
        stringArray = []

if stringArray:
    arrayArray.append(stringArray)

for i in arrayArray:
    for j in i:
        s += j
    pfd_solve(StringIO.StringIO(s), sys.stdout)
    sys.stdout.write("\n")
    s = ""
