from common.pairs import *
from compound_data.Vector import *


def mak_rect(origin, horiz, vert):
    return cons(origin, cons(horiz, vert))


def get_origin(rect):
    return car(rect)


def get_horiz(rect):
    return cdr(car(rect))


def get_vert(rect):


def mak_pict(rect):
    return lambda rect: 

def coord_map(rect):
    return lambda point: