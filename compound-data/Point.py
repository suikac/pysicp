from common.Pairs import *


def mak_point(x, y):
    return cons(x, y)


def x_cord(p):
    return car(p)


def y_cord(p):
    return cdr(p)


def equal_point(p1, p2):
    return x_cord(p1) == x_cord(p2) and y_cord(p1) == y_cord(p2)