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

from PFD import pfd_solve

# ----
# main
# ----

pfd_solve(sys.stdin, sys.stdout)
