from Pair import *


def mak_list():
    return None


def append(element, arr):
    return cons(element, arr)


def remove(index, arr, cur):
    return append(cur, cdr(arr)) if index == 0 else remove(index - 1, tail(arr), append(cur, car(arr)))


def head(arr):
    return car(arr)


def tail(arr):
    return cdr(arr)


def get(index, arr):
    return head(arr) if index == 0 else get(index - 1, tail(arr))
