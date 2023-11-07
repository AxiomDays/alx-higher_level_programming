#!/usr/bin/python3
def multiple_returns(sentence):
    if (len(sentence) < 1):
        return None
    tuple = (len(sentence), list(sentence)[0])
    return tuple
