#!/usr/bin/python3
""" function that turns a json file into an object """
import json

def load_from_json_file(filename):
    """ the function in question """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.loads(f.read())
