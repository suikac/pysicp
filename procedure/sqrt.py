dx = 0.000001  # dx in derivative


# return the square root of x
def sqrt(x):
    return _try_guess(x, 1)


def _try_guess(x, guess):
    return guess if _good_enough(x, guess) else _try_guess(x, _improve(x, guess))


def _good_enough(x, y):
    return abs(x - y * y) < 0.001


# improve the guess of sqrt
def _improve(x, y):
    return _average(y, x / y)


def _average(x, y):
    return (x + y) / 2.0


def _newton(x, y):
    pass


def derivative(x, y):
    pass
