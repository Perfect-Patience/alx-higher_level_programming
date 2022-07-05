#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        val1 = 0
    else:
        val1 = tuple_a[0]
    if len(tuple_b) == 0:
        val2 = 0
    else:
        val2 = tuple_b[0]
    if len(tuple_a) < 2:
        val3 = 0
    else:
        val3 = tuple_a[1]
    if len(tuple_b) < 2:
        val4 = 0
    else:
        val4 = tuple_b[1]
    return (val1 + val2, val3 + val4)
