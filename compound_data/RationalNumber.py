"""
rational number implementation
"""
from common.pairs import *
from common.arith import *


# a make-rat that simplify when construct
def make_rat(numer, denom):
    return cons(numer / gcd(numer, denom),
                denom / gcd(numer, denom))


def get_numer(x):
    return car(x)


def get_denom(x):
    return cdr(x)


def multi_rat(x, y):
    return make_rat(
        get_numer(x) * get_denom(y) + get_numer(y) * get_denom(x),
        get_denom(x) * get_denom(y)
    )

