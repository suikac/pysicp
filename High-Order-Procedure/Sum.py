"""
Sequential sum implementation
"""


# represent a general form of sequential summing
def seq_sum(step, incr, start, stop):
    return _seq_sum(step, incr, 0, start, stop)


def _seq_sum(step, incr, cur, start, stop):
    return cur if start > stop else _seq_sum(step, incr, cur + incr(start), step(start), stop)
