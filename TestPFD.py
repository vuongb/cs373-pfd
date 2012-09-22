#!/usr/bin/env python

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2012
# Glenn P. Downing
# -------------------------------

"""
To test the program:
    % python TestCollatz.py >& TestCollatz.py.out
    % chmod ugo+x TestCollatz.py
    % TestCollatz.py >& TestCollatz.py.out
"""

# -------
# imports
# -------

import StringIO
import unittest

from PFD import pfd_read, pfd_eval, pfd_print, pfd_solve

# -----------
# TestPFD
# -----------

class TestPFD (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read_1 (self) :
        r = StringIO.StringIO("1 10\n")
        a = []
        b = pfd_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 10)

    def test_read_2 (self) :
        r = StringIO.StringIO("40 50 60 80\n")
        a = []
        b = pfd_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  40)
        self.assert_(a[1] == 50)
        self.assert_(a[2] == 60)
        self.assert_(a[3] == 80)

    def test_read_3 (self) :
        r = StringIO.StringIO("-1 5 8")
        a = []
        b = pfd_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  -1)
        self.assert_(a[1] == 5)
        self.assert_(a[2] == 8)

    def test_read_4 (self) :
        r = StringIO.StringIO("87 42 0 92 56\n")
        a = []
        b = pfd_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  87)
        self.assert_(a[1] == 42)
        self.assert_(a[2] == 0)
        self.assert_(a[3] == 92)
        self.assert_(a[4] == 56)

    # ----
    # eval
    # ----

	def test_eval_1 (self) :
		a = [1,2]
		listOrder.append(a)
		a = [3,4,5]
		listOrder.append(a)
		pfd_eval(listOrder)
        #self.assert_(v == 20)

##    def test_eval_2 (self) :
##        n = 50000
##        preCompArray = [0]*n
##        collatz_createCache(50000, preCompArray)
##        v = collatz_eval(100, 200, preCompArray)
##        self.assert_(v == 125)
##
##    def test_eval_3 (self) :
##        n = 50000
##        preCompArray = [0]*n
##        collatz_createCache(50000, preCompArray)
##        v = collatz_eval(201, 210, preCompArray)
##        self.assert_(v == 89)
##
##    def test_eval_4 (self) :
##        n = 50000
##        preCompArray = [0]*n
##        collatz_createCache(50000, preCompArray)
##        v = collatz_eval(900, 1000, preCompArray)
##        self.assert_(v == 174)
##        
##    def test_eval_5 (self) :
##        n = 50000
##        preCompArray = [0]*n
##        collatz_createCache(50000, preCompArray)
##        v = collatz_eval(972699, 998031, preCompArray)
##        self.assert_(v == 440)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO.StringIO()
        a = [1, 10, 20]
        pfd_print(w, a)
        self.assert_(w.getvalue() == "1 10 20")

    def test_print_2 (self) :
        w = StringIO.StringIO()
        a = [100, 200, 125, 400, 8, 7]
        pfd_print(w, a)
        self.assert_(w.getvalue() == "100 200 125 400 8 7")

    def test_print_3 (self) :
        w = StringIO.StringIO()
        a = [201, 210, 89, 1, 2, 100, 500]
        pfd_print(w, a)
        self.assert_(w.getvalue() == "201 210 89 1 2 100 500")

    def test_print_4 (self) :
        w = StringIO.StringIO()
        a = [900, 1000, 174, 41, 87, 5, 2]
        pfd_print(w, a)
        self.assert_(w.getvalue() == "900 1000 174 41 87 5 2")
        

    def test_print_5 (self) :
        w = StringIO.StringIO()
        a = [972699, 998031, 440]
        pfd_print(w, a)
        self.assert_(w.getvalue() == "972699 998031 440")


    # -----
    # solve
    # -----

##    def test_solve_1 (self) :
##        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
##        w = StringIO.StringIO()
##        collatz_solve(r, w)
##        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
##
##    def test_solve_2 (self) :
##        r = StringIO.StringIO("43423 32909\n11900 20067\n201 210\n6988 45692\n")
##        w = StringIO.StringIO()
##        collatz_solve(r, w)
##        self.assert_(w.getvalue() == "43423 32909 324\n11900 20067 279\n201 210 89\n6988 45692 324\n")
##
##    def test_solve_3 (self) :
##        r = StringIO.StringIO("1 2\n10 2\n")
##        w = StringIO.StringIO()
##        collatz_solve(r, w)
##        self.assert_(w.getvalue() == "1 2 2\n10 2 20\n")
##
##    def test_solve_4 (self) :
##        r = StringIO.StringIO("63500 798004\n3209 689943\n293 38\n888888 999999\n")
##        w = StringIO.StringIO()
##        collatz_solve(r, w)
##        self.assert_(w.getvalue() == "63500 798004 509\n3209 689943 509\n293 38 128\n888888 999999 507\n")

# ----
# main
# ----

print "TestPFD.py"
unittest.main()
print "Done."
