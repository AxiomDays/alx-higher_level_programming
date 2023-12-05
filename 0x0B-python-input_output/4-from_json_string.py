#!/usr/bin/python3
""" this is a file holding a function that  returns an object (Python data structure) represented by a JSON string """
import json

def from_json_string(my_str):
    """ the fxn in question """
    return json.loads(my_str)
