"""
Pair implementation
"""


def cons(a, b):
    return lambda x: a if x == 1 else b if x == 2 else None


def car(x):
    return x(1)


def cdr(x):
    return x(2)


def equal_pair(p1, p2):
    return car(p1) == car(p2) and cdr(p1) == cdr(p2)
