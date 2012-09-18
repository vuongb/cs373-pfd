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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_createCache

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read_1 (self) :
        r = StringIO.StringIO("1 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 10)

    def test_read_2 (self) :
        r = StringIO.StringIO("1 100\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 100)

    def test_read_3 (self) :
        r = StringIO.StringIO("54 250\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  54)
        self.assert_(a[1] == 250)

    def test_read_4 (self) :
        r = StringIO.StringIO("521 522\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  521)
        self.assert_(a[1] == 522)

    def test_read_5 (self) :
        r = StringIO.StringIO("54 54\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  54)
        self.assert_(a[1] == 54)

    def test_read_6 (self) :
        r = StringIO.StringIO("65 4\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  65)
        self.assert_(a[1] == 4)

    def test_read_7 (self) :
        r = StringIO.StringIO("04 09\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  4)
        self.assert_(a[1] == 9)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        n = 50000
        preCompArray = [0]*n
        collatz_createCache(50000, preCompArray)
        v = collatz_eval(1, 10, preCompArray)
        self.assert_(v == 20)

    def test_eval_2 (self) :
        n = 50000
        preCompArray = [0]*n
        collatz_createCache(50000, preCompArray)
        v = collatz_eval(100, 200, preCompArray)
        self.assert_(v == 125)

    def test_eval_3 (self) :
        n = 50000
        preCompArray = [0]*n
        collatz_createCache(50000, preCompArray)
        v = collatz_eval(201, 210, preCompArray)
        self.assert_(v == 89)

    def test_eval_4 (self) :
        n = 50000
        preCompArray = [0]*n
        collatz_createCache(50000, preCompArray)
        v = collatz_eval(900, 1000, preCompArray)
        self.assert_(v == 174)
        
    def test_eval_5 (self) :
        n = 50000
        preCompArray = [0]*n
        collatz_createCache(50000, preCompArray)
        v = collatz_eval(972699, 998031, preCompArray)
        self.assert_(v == 440)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print_2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 100, 200, 125)
        self.assert_(w.getvalue() == "100 200 125\n")

    def test_print_3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 201, 210, 89)
        self.assert_(w.getvalue() == "201 210 89\n")

    def test_print_4 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 900, 1000, 174)
        self.assert_(w.getvalue() == "900 1000 174\n")
        

    def test_print_5 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 972699, 998031, 440)
        self.assert_(w.getvalue() == "972699 998031 440\n")

    def test_print_6 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 10, 2, 20)
        self.assert_(w.getvalue() == "10 2 20\n")

    def test_print_7 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 43423, 32909, 324)
        self.assert_(w.getvalue() == "43423 32909 324\n")

    def test_print_8 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 63500, 798004, 509)
        self.assert_(w.getvalue() == "63500 798004 509\n")

    

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO.StringIO("43423 32909\n11900 20067\n201 210\n6988 45692\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "43423 32909 324\n11900 20067 279\n201 210 89\n6988 45692 324\n")

    def test_solve_3 (self) :
        r = StringIO.StringIO("1 2\n10 2\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 2 2\n10 2 20\n")

    def test_solve_4 (self) :
        r = StringIO.StringIO("63500 798004\n3209 689943\n293 38\n888888 999999\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "63500 798004 509\n3209 689943 509\n293 38 128\n888888 999999 507\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
