#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    factor = 2
    nu_dict = {key: value * factor for key, value in a_dictionary.items()}
    return nu_dict
