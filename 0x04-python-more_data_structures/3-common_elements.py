#!/usr/bin/python3
def common_elements(set_1, set_2):
    nulist = []
    for i in set_1:
        for j in set_2:
            if (j == i):
                nulist.append(j)
    return nulist
