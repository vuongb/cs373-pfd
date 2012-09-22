#!/usr/bin/env python

# ---------------------------
# projects/pfd/PFD.py
# Copyright (C) 2012
# Glenn P. Downing
# ---------------------------

from pprint import pprint #used to printout matrix (debugging)


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
    assert s != ""
    if s == "" :
        return False
    l = s.split()
    for item in l:
        a.append(int(item))
    return True
# -------------
# pfd_print
# -------------

def pfd_print (w, listOrder) :
    """
    prints the values contained in listOrder
    w is a writer
    listOrder is a list of the topologically sorted task numbers
    """
    
    for i in range(len(listOrder)):

        assert listOrder[i] > 0
        
        if (i == len(listOrder)-1):
            w.write(str(listOrder[i]))
        else:
            w.write(str(listOrder[i]) + " ")

# ------------
# pfd_eval
# ------------


def pfd_eval (a, w) :
    """
    a is an array of array with all values read in
    """

    #The two elements from the first time give us:
    #The number of tasks and the number of subsequent lines
    taskNum = (a[0])[0]
    lineNum = (a[0])[1]
    
    #Make sure both taskNum and lineNum will be positive
    assert taskNum > 0
    assert lineNum > 0

    #Builds the adjacency matrix
    adjMatrix = []
    for i in range(taskNum):
        relations = [0]*taskNum  #populating the matrix with 0's (replace with 1 if there is a relation)
        pprint(relations)
        adjMatrix.append(relations)
    
    #Populates the value of adjMatrix
    for j in range(1, 1 + lineNum):
        curr = a[j] #Current line from reader
        val = curr[0] #value
        num = curr[1] #number of relations this value has
        
        #Make sure values are positive
        assert val > 0
        assert num > 0
        for k in range(2, 2 + num):
            rel = curr[k] #relationship (prerequisite) for val
            #debugging
            asdf = adjMatrix[val-1]
            fdsa = asdf[rel-1]
            (adjMatrix[val-1])[rel-1] = 1 #change the relationship value to 1
    print("Adjacency Matrix: ")
    pprint(adjMatrix)
        
    #Now to solve
    #4 Steps:
    #1 Create list of values with no prereqs
    #2 Select lowest value from list and add to answer
    #3 Remove all prereqs of this value
    #4 Repeat Steps 1-3 until answer is fully populated

# -----------
# 


# -------------
# pfd_solve
# -------------

def pfd_solve (r, w) :
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
