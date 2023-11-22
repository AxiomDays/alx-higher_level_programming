#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i=0
    for j in range(x):
        try:
            i=i+1
            print("{:d}".format(my_list[j]), end =" ")
        except IndexError:
            break
    return i
