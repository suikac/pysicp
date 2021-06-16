from common.Pair import *


def mak_point():  # can be also named as procedure
    return cons


def x_cord():
    return car


def y_cord():
    return cdr


def add_point(p1, p2):
    return mak_point()(
        x_cord()(p1) + x_cord()(p2),
        y_cord()(p1) + y_cord()(p2)
    )


def scale(s, p):
    return mak_point()(
        s * x_cord()(p),
        s * y_cord()(p)
    )


def equal_point(p1, p2):
    return x_cord()(p1) == x_cord()(p2) and y_cord()(p1) == y_cord()(p2)
