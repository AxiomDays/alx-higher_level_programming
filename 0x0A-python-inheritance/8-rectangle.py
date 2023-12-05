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

class Rectangle(BaseGeometry):
    """ class that inherits from basegeometry """
    def __init__(self, width, height):
        """ regular init """
        self.integer_validator("width", width)
        self.__width=width
        self.integer_validator("height", height)
        self.__height=height
