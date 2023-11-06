#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if (len(tuple_a) < 1):
        sum_a = ( 0 + tuple_b[0])
    elif(len(tuple_b) < 1):
        sum_a = (tuple_a[0] + 0 )
    else:
        sum_a = (tuple_a[0] + tuple_b[0])

    if (len(tuple_a) < 2):
        sum_b = ( 0 + tuple_b[1])
    elif(len(tuple_b) < 2):
        sum_b = (tuple_a[1] + 0 )
    else:
        sum_b = (tuple_a[1] + tuple_b[1])

    tuple = (sum_a, sum_b)
    return tuple
