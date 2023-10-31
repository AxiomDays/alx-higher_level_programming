#!/usr/bin/python3
def pow(a, b):
    j = a
    if (b > 1):
        for i in range (b-1):
            j *= a
    elif (b == 0):
        return 1
    elif (b < 0):
        neg_j = 1/j
        for i in range ((b*-1)-1):
            neg_j *= 1/j
        return neg_j
    return j

