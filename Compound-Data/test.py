import unittest
from RationalNumber import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        rat = make_rat(6, 8)
        self.assertEqual(get_numer(rat), 3)
        self.assertEqual(get_denom(rat), 4)


if __name__ == '__main__':
    unittest.main()
