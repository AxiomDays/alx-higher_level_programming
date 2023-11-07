#!/usr/bin/python3
def multiple_returns(sentence):
    char = list(sentence)[0]
    if (len(sentence) < 1):
        char = None
    tuple = (len(sentence), char)
    return tuple
