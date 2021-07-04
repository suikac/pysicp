import unittest
from Rectangle import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        p1 = mak_vec()(1, 2)
        p2 = mak_vec()(3, 4)
        p3 = mak_vec()(5, 6)
        p4 = mak_vec()(7, 8)
        r = mak_rect(0, 2, 3)
        g = mak_picture(mak_seg(p1, p2), mak_seg(p3, p4))
        g(r)


if __name__ == '__main__':
    unittest.main()
