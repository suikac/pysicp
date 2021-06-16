import unittest
from LineSegment import *
from RationalNumber import *


class TestRat(unittest.TestCase):
    def test_rat(self):
        rat = make_rat(6, 8)
        rat2 = make_rat(8, 10)
        self.assertEqual(get_numer(rat), 3)
        self.assertEqual(get_denom(rat), 4)
        self.assertEqual(get_numer(multi_rat(rat2, rat)), 31)
        self.assertEqual(get_denom(multi_rat(rat2, rat)), 20)


class TestLineSeg(unittest.TestCase):
    def test_line_seg(self):
        p1 = mak_point()(3, 4)
        p2 = mak_point()(7, 1)
        line1 = mak_seg(p1, p2)
        self.assertEqual(equal_point(mid_point(line1), mak_point()(5, 2.5)), True)


if __name__ == '__main__':
    unittest.main()
