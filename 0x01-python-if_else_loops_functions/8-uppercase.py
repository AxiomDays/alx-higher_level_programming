#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if (ord(i) > 90):
            j = chr(ord(i) - 32)
            print("{:s}".format(j), end = "")
        else:
            print(i, end = '')
    print("")
