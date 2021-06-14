"""
Unit Test for common
"""

import unittest
from Pair import *
from Arith import *
from List import *


class TestPair(unittest.TestCase):
    def test_pair_axiom(self):
        a = cons(3, 4)
        self.assertEqual(car(a), 3)
        self.assertEqual(cdr(a), 4)


class TestArith(unittest.TestCase):
    def test_gcd(self):
        self.assertEqual(gcd(4, 6), 2)
        self.assertEqual(gcd(13, 26), 13)


class TestList(unittest.TestCase):
    def test_list(self):
        list1 = mak_list()
        list2 = mak_list()
        list3 = append(4, list1)
        self.assertEqual(get(0, list3), 4)


if __name__ == '__main__':
    unittest.main()
