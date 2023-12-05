#!/usr/bin/python3
""" function to tell if an object is a an instance of a subclass """
def inherits_from(obj, a_class):
    """ the function in question """
    if issubclass(type(obj), a_class):
        if (type(obj) != a_class):
            return True
