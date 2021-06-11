import unittest
from Pairs import *
from Arith import *


class TestPair(unittest.TestCase):
    def test_pair_axiom(self):
        a = cons(3, 4)
        self.assertEqual(car(a), 3)
        self.assertEqual(cdr(a), 4)


class TestArith(unittest.TestCase):
    def test_gcd(self):
        self.assertEqual(gcd(4, 6), 2)
        self.assertEqual(gcd(13, 26), 13)


if __name__ == '__main__':
    unittest.main()
