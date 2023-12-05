#!/usr/bin/python3
""" Function that reads a file """
def read_file(filename=""):
    """ the fxn in question """
    with open(filename, 'r', encoding="utf-8") as f:
        reader = f.read()
        print(reader, end="")
