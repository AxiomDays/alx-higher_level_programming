#!/usr/bin/bash

def class_to_json(obj):
    """
    Convert an object into a dictionary with simple data structures for JSON serialization.

    Args:
    - obj: The object to be converted.

    Returns:
    - A dictionary with simple data structures.
    """
    return obj.__dict__
