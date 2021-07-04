"""
Unit Test for common
"""

import unittest
from pairs import *
from arith import *
from self_list import *


class TestPair(unittest.TestCase):
    def test_pair_axiom(self):
        a = cons(3, 4)
        self.assertEqual(car(a), 3)
        self.assertEqual(cdr(a), 4)

    def test_wired_pair(self):
        p1 = cons(1, None)
        p2 = cons(p1, cons(2, None))
        print(car(car(p2)))


class TestArith(unittest.TestCase):
    def test_gcd(self):
        self.assertEqual(gcd(4, 6), 2)
        self.assertEqual(gcd(13, 26), 13)


class TestList(unittest.TestCase):
    def test_mak_list(self):
        list1 = mak_list(1, 2, 3, 4, 5, 6)
        self.assertEqual(get(2, list1), 3)

    def test_insert(self):
        list1 = mak_list(1, 2, 3, 4)
        list2 = insert(8, list1)
        self.assertEqual(get(0, list2), 8)

    def test_remove(self):
        list1 = mak_list(1, 2, 3, 4, 5)
        list2 = remove(3, list1)
        self.assertEqual(get(3, list2), 5)

    def test_json(self): # try to make a json using list
        json1 = mak_list(cons(1, mak_list("hello", "I", "am")),
                         cons("hee", "4"))


if __name__ == '__main__':
    unittest.main()
