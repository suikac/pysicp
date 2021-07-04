import unittest
from Rectangle import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        p1 = mak_vec(1, 2)
        p2 = mak_vec(3, 4)
        p3 = mak_vec(5, 6)
        p4 = mak_vec(7, 8)
        r = mak_rect(mak_vec(0, 0), mak_seg(0, 4), mak_seg(5, 0))
        g = mak_picture([mak_seg(p1, p2), mak_seg(p3, p4)])
        g(r)

    def _helper(self, col):
        for el in col:
            print(el)

    def _helper2(self, *el):
        self._helper(el)

    def test_s(self):
        self._helper2(1, 2, 3, 4)


if __name__ == '__main__':
    unittest.main()
