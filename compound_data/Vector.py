from common.pairs import *


def mak_vec():  # can be also named as procedure
    return cons


def x_cord():
    return car


def y_cord():
    return cdr


def add_vec(p1, p2):
    return mak_vec()(
        x_cord()(p1) + x_cord()(p2),
        y_cord()(p1) + y_cord()(p2)
    )


def scale(s, p):
    return mak_vec()(
        s * x_cord()(p),
        s * y_cord()(p)
    )


def equal_point(p1, p2):
    return x_cord()(p1) == x_cord()(p2) and y_cord()(p1) == y_cord()(p2)
