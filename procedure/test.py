import unittest
from sqrt import *


class TestSqrt(unittest.TestCase):
    def test_sqrt(self):
        self.assertEqual(sqrt(9) - 3 < 0.0001, True)
        self.assertEqual(sqrt(25) - 5 < 0.0001, True)
        self.assertEqual(sqrt(144) - 12 < 0.0001, True)


if __name__ == '__main__':
    unittest.main()
