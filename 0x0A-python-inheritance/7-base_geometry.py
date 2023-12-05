#!/usr/bin/python3
""" class called base geometry """

class BaseGeometry():
    """ the class in question """
    def area(self):
        """ function that raises a unqiue exception """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """ Function for checking the params of values """
        if (type(value) is not int):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
