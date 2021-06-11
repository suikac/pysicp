import unittest
from Pairs import *


class TestPair(unittest.TestCase):
    def test_pair_axiom(self):
        a = cons(3, 4)
        self.assertEqual(car(a), 3)
        self.assertEqual(cdr(a), 4)


if __name__ == '__main__':
    unittest.main()
