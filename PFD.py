#!/usr/bin/env python

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2012
# Glenn P. Downing
# ---------------------------


# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2012
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

def collatz_read (r, a) :
    """
    reads two ints into a[0] and a[1]
    r is a  reader
    a is an array of int
    return true if that succeeds, false otherwise
    """
    s = r.readline()
    if s == "" :
        return False
    l = s.split()
    a[0] = int(l[0])
    a[1] = int(l[1])
    assert a[0] > 0
    assert a[1] > 0
    return True

# ------------
# collatz_eval
# ------------

##def collatz_eval (i, j) :
def collatz_eval (i, j, a) :
    """
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    return the max cycle length in the range [i, j]
    Need to pass the pre-Computed Array as an argument
    """
    assert i > 0
    assert j > 0
    
    b = min(i,j)
    c = max(i,j)

    assert b <= c

#-----------------------------------------------------------
# Lazy Cache Algorithm
##    cycleMax = 0
##    n = 1000000
##    cacheArray = [0] * n
##    cacheArray[0] = 1
##    for x in range(b, c+1):
##        num = x
##        
##        if (cacheArray[x-1] != 0):
##            cycleMax = max(cycleMax, cacheArray[x-1])
##        else:
##            addList = []
##            while(num != 1 and ((num-1) >= n or ((num-1) < n and cacheArray[num-1] == 0))):
##                if( (num-1) < n):
##                    addList.append(num)
##                for item in addList:
##                    cacheArray[item-1] += 1
##                if (num % 2 == 0):
##                    num /= 2
##                else:
##                    num = (3*num)+1
##
##            for item in addList:
##                cacheArray[item-1] += cacheArray[num-1]
##            cycleMax = max(cycleMax, cacheArray[x-1])
##            
##    assert cycleMax > 0
##    return cycleMax

  
#-----------------------------------------------------------
# Dumb Algorithm
##    cycleMax = 0
##    for x in range(b, c+1):
##        count = 1
##        while (x != 1):
##            #count += 1
##            if x % 2 == 0:
##                x /= 2
##                count += 1
##            else:
##                x = x + (x >> 1) + 1
##                count += 2
##        cycleMax = max(count, cycleMax)
##    assert cycleMax > 0
##    return cycleMax


#-----------------------------------------------------------
# Eager cache  
    cycleMax = 0
    n = 50000
    for x in range(b,c+1):
        assert x > 0
        count = 1
        if x <= n:
            cycleMax = max(cycleMax, a[x-1])
        else:
            while (x != 1 and x > n):
                if x % 2 == 0:
                    x /= 2
                else:
                    x = (3*x) + 1
                    
                if x <= n:
                    count += a[x-1]
                else:
                    count += 1
            assert count > 0
            cycleMax = max(cycleMax, count)
            
    assert cycleMax > 0
    return cycleMax

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    prints the values of i, j, and v
    w is a writer
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    v is the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    Need to create precomputed cache array
    """
#-----------------------------------------------------------
# Eager cache  
##    n = 100000
##    preCompArray = [0]*n
##    for ind in range(n):
##        findNum = ind + 1
##        count = 1
##        while (findNum != 1 and ((findNum-1) >= n or preCompArray[findNum - 1] == 0)):
##            if (findNum % 2) == 0:
##                findNum /= 2
##                if ((findNum-1) >= n or ((findNum - 1) < n and preCompArray[findNum-1] == 0)):
##                    count += 1
##            else:
##                findNum = findNum + (findNum >> 1) + 1
##                if ((findNum-1) >= n or ((findNum - 1) < n and preCompArray[findNum-1] == 0)):
##                    count += 2
##        if(preCompArray[findNum - 1] != 0):
##            count += preCompArray[findNum - 1]
##        preCompArray[ind] = count
    n = 50000
    preCompArray = [0]*n
    collatz_createCache(n, preCompArray)

    assert preCompArray[0] > 0
    assert preCompArray[n-1] > 0
    
    a = [0, 0]
    while collatz_read(r, a) :
        v = collatz_eval(a[0], a[1], preCompArray)
        collatz_print(w, a[0], a[1], v)

#-----------------------------------------------------------
# Dumb Algorithm/Lazy Cache
##    a = [0, 0]
##    while collatz_read(r, a) :
##        v = collatz_eval(a[0], a[1], w)
##        collatz_print(w, a[0], a[1], v)

# -------------
# collatz_EagerCache
# -------------

def collatz_createCache (n, preCompArray) :
    """
    Find the cycle length for each value up to n
    Array index, i, corresponds with the number i+1
    """
    
    for ind in range(n):
        findNum = ind + 1
        count = 1
        while (findNum != 1 and ((findNum-1) >= n or preCompArray[findNum - 1] == 0)):
            if (findNum % 2) == 0:
                findNum /= 2
                if ((findNum-1) >= n or ((findNum - 1) < n and preCompArray[findNum-1] == 0)):
                    count += 1
            else:
                findNum = findNum + (findNum >> 1) + 1
                if ((findNum-1) >= n or ((findNum - 1) < n and preCompArray[findNum-1] == 0)):
                    count += 2
        if(preCompArray[findNum - 1] != 0):
            count += preCompArray[findNum - 1]
        assert count > 0
        preCompArray[ind] = count
