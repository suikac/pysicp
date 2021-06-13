import unittest
from sqrt import *


class TestSqrt(unittest.TestCase):
    def test_sqrt(self):
        self.assertEqual(sqrt(4) - 2 < 0.0001, True)


if __name__ == '__main__':
    unittest.main()
