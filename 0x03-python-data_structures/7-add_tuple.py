#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    pos = 0
    tuple_res = ()
    while (pos < 2):
        if (len(tuple_a) < 2):
            tuple_a.append(0)
        if (len(tuple_b) < 2):
            tuple_b.append(0)
        tuple_res.append(tuple_a[pos] + tuple_b[pos])
        pos = pos + 1
    return (tuple_res)
