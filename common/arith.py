"""
Arithmetic computation
"""


# return the greatest common divider of a and b
def gcd(a, b):
    return b if a == 0 else a if b == 0 else gcd(b, a % b)


def avg(*args):
    count = 0
    cur_sum = 0
    for arg in args:
        count += 1
        cur_sum += arg
    return cur_sum * 1.0 / count
