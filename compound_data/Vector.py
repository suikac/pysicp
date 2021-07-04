from common.pairs import *


def mak_vec(x, y):  # can be also named as procedure
    return cons(x, y)


def x_cord(v):
    return car(v)


def y_cord(v):
    return cdr(v)


def add_vec(p1, p2):
    return mak_vec(
        x_cord(p1) + x_cord(p2),
        y_cord(p1) + y_cord(p2)
    )


def scale(s, p):
    return mak_vec(
        s * x_cord(p),
        s * y_cord(p)
    )


def equal_point(p1, p2):
    return x_cord(p1) == x_cord(p2) and y_cord(p1) == y_cord(p2)


def vec_to_str(p):
    return "({}, {})".format(x_cord(p), y_cord(p))


def drawline(p1, p2):
    print("a line is drew between {} and {}".format(vec_to_str(p1), vec_to_str(p2)))
