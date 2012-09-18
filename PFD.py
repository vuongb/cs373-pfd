#!/usr/bin/env python

# ---------------------------
# projects/pfd/PFD.py
# Copyright (C) 2012
# Glenn P. Downing
# ---------------------------

# ------------
# pfd_read
# ------------

def pfd_read (r, a) :
    """
    reads ints into a
    r is a  reader
    a is an array of int
    return true if that succeeds, false otherwise
    """
    s = r.readline()
    if s == "" :
        return False
    l = s.split()
    for item in l:
        a.append(int(item))
    for item in a:
        assert item > 0
    return True
# -------------
# pfd_print
# -------------

def collatz_print (w, listOrder) :
    """
    prints the values contained in listOrder
    w is a writer
    listOrder is a list of the topologically sorted task numbers
    """
    for item in listOrder:
        w.write(str(item) + " ")
    w.write("\n")

# ------------
# pfd_eval
# ------------

def collatz_eval (a) :
    """
    
    """
    


# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """ 
    read loop, eval, print
    r is a reader
    w is a writer
    """
    a = []
    lineArray = []
    while pfd_read(r, a):
        lineArray.append(a)
        a = []
    l = pfd_eval(lineArray)
    pfd_print(w, l)
