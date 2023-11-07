#!/usr/bin/python3
def multiple_returns(sentence):
    if (len(sentence) < 1):
        char = None
    else:
        char = list(sentence)[0]
    tuple = (len(sentence), char)
    return tuple
