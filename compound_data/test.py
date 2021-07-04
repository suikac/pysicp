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


p1 = mak_vec(3, 4)
p2 = mak_vec(7, 1)


class TestLineSeg(unittest.TestCase):
    def test_vec(self):
        self.assertEqual(x_cord(p1), 3)

    def test_line_seg(self):
        line1 = mak_seg(p1, p2)
        self.assertEqual(equal_point(mid_point(line1), mak_vec(5, 2.5)), True)
        self.assertEqual(equal_point(start_point(line1), mak_vec(3, 4)), True)

    def test_draw_line(self):
        p1 = mak_vec(3, 4)
        p2 = mak_vec(4, 5)
        draw_line(p1, p2)


if __name__ == '__main__':
    unittest.main()
