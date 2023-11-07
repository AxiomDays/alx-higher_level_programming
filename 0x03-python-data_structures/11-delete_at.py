#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    nu_list = []
    count = 0
    if (idx < 0):
        return my_list
    elif (idx > (len(my_list) -1)):
        return my_list
    else:
        for i in my_list:
            if (count == idx):
                count += 1
                continue
            nu_list.append(i)
            count += 1
        my_list.clear()
        for j in nu_list:
            my_list.append(j)
        return nu_list
