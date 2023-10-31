#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if (ord(i) > 90):
            j = chr(ord(i) - 32)
        else:
            j = i
        print("{:s}".format(j), end = "")
    print("")
            
