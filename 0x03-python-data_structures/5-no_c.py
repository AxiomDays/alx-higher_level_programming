#!/usr/bin/python3
def no_c(my_string):
    arr = list(my_string)
    j = 0
    str = ""
    for i in arr:
        if (i == 'c' or i == 'C'):
            arr.pop(j)
        j += 1
    return str.join(arr)
