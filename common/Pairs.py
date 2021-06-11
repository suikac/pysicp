def cons(a, b):
    return lambda x: a if x == 1 else b if x == 2 else None


def car(x):
    return x(1)


def cdr(x):
    return x(2)
