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
    def area(self):
        """ function that return the area of the rect """
        return(self.__height*self.__width)
    def __str__(self):
        """ the str method """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

class Square(Rectangle):
    """ class that inherits from rectangle """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size=size
        super().__init__(size, size)
    def area(self):
        """ area of a square """
        return(self.__size**2)

