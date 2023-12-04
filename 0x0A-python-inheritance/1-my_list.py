#!/usr/bin/python3
""" a class that inherits list """

class MyList(list):
    """ the class in question """
    def __init__(self):
        """ useless init fxn """
        pass
    def print_sorted(self):
        """ the printer fxn """
        print(sorted(self))


