#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_0 = (0, 0)
    if len(tuple_a) < 2:
        tuple_a = tuple(map(sum, zip(tuple_a, tuple_0)))
    if len(tuple_b) < 2:
        tuple_b = tuple(map(sum, zip(tuple_b, tuple_0)))

    slicet = slice(2)
    if len(tuple_a) > 2:
        tuple_a = tuple_a[slicet]
    if len(tuple_b) > 2:
        tuple_b = tuple_b[slicet]

    return tuple(map(lambda ta, tb: ta + tb, tuple_a, tuple_b))
