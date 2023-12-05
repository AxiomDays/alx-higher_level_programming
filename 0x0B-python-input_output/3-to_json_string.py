#!/usr/bin/python3
""" converting python to json """
import json

def to_json_string(my_obj):
    """ function that does that and returns the object """
    buff=json.dumps(my_obj)
    return buff
