#!/usr/bin/python3
def best_score(a_dict):
    if a_dict and len(a_dict):
        max = list(a_dict.keys())[0]
        for key in a_dict:
            if a_dict[key] > a_dict[max]:
                max = key
        return max
    return None
