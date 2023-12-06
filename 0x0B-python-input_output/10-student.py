#!/usr/bin/python3
""" class meant to turn an object tojson format """
class Student():
    """ the class in question """
    def __init__(self, first_name, last_name, age):
        """ init function """
        self.first_name=first_name
        self.last_name=last_name
        self.age=age

    def to_json(self, attrs=None):
        """ the jsonification """
        return self.__dict__

