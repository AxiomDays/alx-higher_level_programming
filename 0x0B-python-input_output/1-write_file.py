#!/usr/bin/python3
""" program to write to a file """

def write_file(filename="", text=""):
    """ the function of the hour """
    with open(filename, 'w', encoding="utf-8") as g:
        writ = g.write(text)
        return writ
