import unittest
from Sum import *


class MyTestCase(unittest.TestCase):
    def test_seq_sum(self):
        k = seq_sum(lambda x: x + 1, lambda x: x*2, 0, 4)
        self.assertEqual(k, 20)


if __name__ == '__main__':
    unittest.main()
