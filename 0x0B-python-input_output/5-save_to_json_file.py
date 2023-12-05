#!/usr/bin/python3
""" turns a object into json then saves to a file """
import json

def save_to_json_file(my_obj, filename):
    """ the function in question """
    y=json.dumps(my_obj)
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(y)
