from Vector import *


# Basic line interface
def mak_seg(x, y):
    return cons(x, y)


def start_point(x):
    return car(x)


def end_point(x):
    return cdr(x)


# line function based on basic interface
def mid_point(line):
    return mak_vec()(
        abs(x_cord()(end_point(line)) + x_cord()(start_point(line))) / 2,
        abs(y_cord()(end_point(line)) + y_cord()(start_point(line))) / 2
    )


def vec_to_str(v):
    return "({}, {})".format(start_point(v), end_point(v))


def draw_line(p1, p2):
    print("a line is drawn between" + vec_to_str(p1) + " " + vec_to_str(p2))


