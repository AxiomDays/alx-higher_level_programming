#!/usr/bin/python3
""" function that appends """
def append_write(filename="", text=""):
    """ the function in question """
    with open(filename, 'a', encoding="utf-8") as h:
        return h.write(text)
