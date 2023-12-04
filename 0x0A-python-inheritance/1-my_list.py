#!/usr/bin/python3
""" a class that inherits list """

class MyList(list):
    """ the class in question """
    def __init__(self):

        """ useless init fxn """
        super().__init__()
        pass
    def print_sorted(self):
        """ the printer fxn """
        print(sorted(self))


