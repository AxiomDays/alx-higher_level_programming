#!/usr/bin/python3
""" function to cehck if an object is an instance of a givrn class """

def is_same_class(obj, a_class):
    """ the function in question """
    if isinstance(obj, a_class):
        return True
    else:
        return False
