#!/usr/bin/env python

# -------------------------------
# projects/collatz/TestPFD.py
# Copyright (C) 2012
# Michael Tarng & Bryan Vuong
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

from PFD import pfd_read, pfd_eval, pfd_print, pfd_solve, pfd_present

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
        listOrder = []
        a = [5,4]
        listOrder.append(a)
        a = [3,2,1,5]
        listOrder.append(a)
        a = [2,2,5,3]
        listOrder.append(a)
        a = [4,1,3]
        listOrder.append(a)
        a = [5,1,1]
        listOrder.append(a)
        l = pfd_eval(listOrder)
        assert l[0] == 1
        assert l[1] == 5
        assert l[2] == 3
        assert l[3] == 2
        assert l[4] == 4
        assert len(l) == 5   

    def test_eval_2 (self) :
        listOrder = []
        a = [3, 2]
        listOrder.append(a)
        a = [1, 2, 2, 3]
        listOrder.append(a)
        a = [2, 1, 3]
        listOrder.append(a)
        l = pfd_eval(listOrder)
        assert l[0] == 3
        assert l[1] == 2
        assert l[2] == 1
        assert len(l) == 3

    def test_eval_3 (self) :
        listOrder = []
        a = [4, 3]
        listOrder.append(a)
        a = [1, 1, 3]
        listOrder.append(a)
        a = [2, 1, 1]
        listOrder.append(a)
        a = [4, 2, 2, 3]
        listOrder.append(a)
        l = pfd_eval(listOrder)
        assert l[0] == 3
        assert l[1] == 1
        assert l[2] == 2
        assert l[3] == 4
        assert len(l) == 4
        

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

    def test_solve_1 (self) :
        r = StringIO.StringIO("5 4\n3 2 1 5\n2 2 5 3\n4 1 3\n5 1 1")
        w = StringIO.StringIO()
        pfd_solve(r, w)
        self.assert_(w.getvalue() == "1 5 3 2 4")

    def test_solve_2 (self) :
        r = StringIO.StringIO("3 2\n1 2 2 3\n2 1 3")
        w = StringIO.StringIO()
        pfd_solve(r, w)
        self.assert_(w.getvalue() == "3 2 1")

    def test_solve_3 (self) :
        r = StringIO.StringIO("4 3\n1 1 3\n2 1 1\n4 2 2 3")
        w = StringIO.StringIO()
        pfd_solve(r, w)
        self.assert_(w.getvalue() == "3 1 2 4")


    # -----
    # present
    # -----    


    def test_present_1 (self) :
        a = [5, 4, 2]
        b = [1, 2, 5, 6]
        pfd_present(b,a)
        assert b[0] == 1
        assert b[1] == 6
        assert len(b) == 2

    def test_present_2 (self) :
        a = [5, 4, 2, 3, 6]
        b = [1,2,5,6]
        pfd_present(b,a)
        assert b[0] == 1
        assert len(b) == 1

    def test_present_3 (self) :
        a = [500, 400, 200]
        b = [1, 2, 5, 6]
        pfd_present(b,a)
        assert b[0] == 1
        assert b[1] == 2
        assert b[2] == 5
        assert b[3] == 6
        assert len(b) == 4

    def test_present_4 (self) :
        a = [5, 4, 2, 1, 6]
        b = [1, 2, 5, 6]
        pfd_present(b,a)
        assert len(b) == 0
        


# ----
# main
# ----

print "TestPFD.py"
unittest.main()
print "Done."
