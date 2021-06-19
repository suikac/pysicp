from pairs import *


def mak_list(*args):
    if args is None:
        return None
    arr = None
    for arg in args:
        arr = append(arg, arr)
    return arr


def append(element, arr):  # append to the end of a list
    return cons(element, None) if arr is None else cons(car(arr), append(element, cdr(arr)))


def insert(element, arr):  # insert to the head of a list
    return cons(element, arr)


def remove(index, arr):
    return cdr(arr) if index == 0 else cons(car(arr), remove(index - 1, cdr(arr)))


def head(arr):
    return car(arr)


def tail(arr):
    return cdr(arr)


def get(index, arr):
    return head(arr) if index == 0 else get(index - 1, tail(arr))


def map_list(f, arr):
    return None if arr is None else cons(f(car(arr)), map_list(f, cdr(arr)))