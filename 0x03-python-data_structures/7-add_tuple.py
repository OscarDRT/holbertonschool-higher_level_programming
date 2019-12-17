#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        tupa = (0, 0)
    if len(tuple_b) == 0:
        tupb = (0, 0)
    if len(tuple_a) == 1:
        tupa = (tuple_a[0], 0)
    if len(tuple_b) == 1:
        tupb = (tuple_b[0], 0)
    if len(tuple_a) >= 2:
        tupa = (tuple_a[0], tuple_a[1])
    if len(tuple_b) >= 2:
        tupb = (tuple_b[0], tuple_b[1])
    tup = (tupa[0] + tupb[0], tupa[1] + tupb[1])
    return tup
