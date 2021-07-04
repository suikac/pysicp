from common.self_list import *
from compound_data.LineSegment import *


def mak_rect(origin, horiz, vert):
    return mak_list(origin, horiz, vert)


def get_origin(rect):
    return get(0, rect)


def get_horiz(rect):
    return get(1, rect)


def get_vert(rect):
    return get(2, rect)


def coord_map(rect):  # for each rect, it returns a map for point
    return lambda vector: add_vec(
        add_vec(scale(x_cord()(vector),
                get_horiz(rect)),
                scale(y_cord()(vector),
                get_vert(rect))),
        get_origin(rect)
    )


def for_each(func, coll):
    for ele in coll:
        func(ele)


def mak_picture(*seg_list):
    return lambda rect: for_each(lambda s: drawline(
        coord_map(rect)(start_point(s)),
        coord_map(rect)(end_point(s))
    ), seg_list)
