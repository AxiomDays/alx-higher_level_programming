#!/usr/bin/python3
"doc for square class with error check"

class Square:
    """
        attributes:
            size (int)
    """
    def __init__(self, size=0):
        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        area=self.__size*self.__size
        return area
