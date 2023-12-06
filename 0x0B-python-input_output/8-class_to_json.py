#!/usr/bin/python3
""" this is what this file does """

def class_to_json(obj):
    """
    Convert an object into a dictionary with simple data structures for JSON serialization.
    """
    return obj.__dict__
