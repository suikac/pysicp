"""
Sequential sum implementation
"""


# represent a general form of sequential summing
def seq_sum(step, incr, start, stop):
    return _seq_sum(step, incr, 0, start, stop)


def harmonic_seq(start, end):
    return _seq_sum(lambda x: x + 1, lambda x: 1 / x, 0, start, end)


def _seq_sum(step, next_term, cur, start, stop):  # Step and and incr act as higher-order-procedure
    return cur if start > stop else _seq_sum(step, next_term, cur + next_term(start), step(start), stop)
