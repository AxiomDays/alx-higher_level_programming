#!/usr/bin/python3
def search_replace(my_list, search, replace):
    count = 0
    nu_list = []
    for i in my_list:
        if (i == search):
            nu_list.append(replace)
            count += 1
        else:
            nu_list.append(i)
            count += 1
    return nu_list
