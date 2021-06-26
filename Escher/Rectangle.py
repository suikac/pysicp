from common.self_list import *
from compound_data.Vector import *


def mak_rect(origin, horiz, vert):
    return mak_list(origin, horiz, vert)


def get_origin(rect):
    return get(0, rect)


def get_horiz(rect):
    return get(1, rect)


def get_vert(rect):
    return get(2, rect)

