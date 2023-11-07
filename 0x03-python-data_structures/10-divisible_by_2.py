#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    nu_list=[]
    for i in my_list:
        if (i % 2 == 0):
            nu_list.append(True)
        else:
            nu_list.append(False)
    return nu_list
