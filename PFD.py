#!/usr/bin/env python

# ---------------------------
# projects/pfd/PFD.py
# Copyright (C) 2012
# Michael Tarng & Bryan Vuong
# ---------------------------

#from pprint import pprint #used to printout matrix (debugging)


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
    #assert s != ""
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


def pfd_eval (a) :
    """
    a is an array of array with all values read in
    """

    #The two elements from the first time give us:
    #The number of tasks and the number of subsequent lines
    taskNum = (a[0])[0]
    lineNum = (a[0])[1]
    
    #Make sure both taskNum and lineNum will be positive
    assert taskNum > 0
    assert lineNum >= 0

    #Builds the adjacency matrix
    adjMatrix = []
    for i in range(taskNum):
        relations = [0]*taskNum  #populating the matrix with 0's (replace with 1 if there is a relation)
#        pprint(relations)
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
            #Make sure the given relationship is valid
            assert rel > 0
            assert rel <= 100
            #debugging
#            asdf = adjMatrix[val-1]
#            fdsa = asdf[rel-1]
            (adjMatrix[val-1])[rel-1] = 1 #change the relationship value to 1
#    print("Adjacency Matrix: ")
#    pprint(adjMatrix)
        
    #Now to solve
    #4 Steps:
    #1 Create list of values with no prereqs
    #2 Select lowest value from list and add to answer
    #3 Remove all prereqs of this value
    #4 Repeat Steps 1-3 until answer is fully populated
    
    answer = []
    while (len(answer) < taskNum):
        poss = []
        #Step 1:
        for i in range(taskNum):
            hasPre = False
            for j in range(taskNum):
                if ((adjMatrix[i])[j] == 1):
                    hasPre = True;
                    break
            if (hasPre == False): #Does not have prereq
                poss.append(i+1)
        
#        print("Debug 1: \n")
#        pprint(answer)
#        pprint(poss)
     
        pfd_present(poss, answer) #removes used answers from next

        #Step 2:
        min = poss[0]
        for i in range(len(poss)):
            if (poss[i] < min):
                min = poss[i]
        answer.append(min)


        #Step 3:
        for i in range(taskNum):
            (adjMatrix[i])[min-1] = 0

#    print("Answer list: ")
#    pprint(answer)
    return answer

# -------------
# pfd_present
# -------------
def pfd_present(n, a) :
    """
    Checks if a value is already in 'a'
    Removes it from 'n', if it is present
    """
    assert len(a) >= 0
#    print "Len a: %d " % (len(a)) 
    assert len(n) >= 0
#    print "Len n: %s " % (str(len(n)))
    count = 0
    while count < len(a):
        for i in range(len(n)):
            if (a[count] == n[i]):
                n.pop(i)
                break; 
        count += 1



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
