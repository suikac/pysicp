"""
rational number implementation
"""
from common.Pairs import *
from common.Arith import *


# a make-rat that simplify when construct
def make_rat(numer, denom):
    return cons(numer / gcd(numer, denom), denom / gcd(numer, denom))


def get_numer(x):
    return car(x)


def get_denom(x):
    return cdr(x)


