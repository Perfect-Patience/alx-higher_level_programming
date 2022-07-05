#!/usr/bin/python3
def multiple_returns(sentence):
    l = len(sentence)
    if (l != 0):
        a = sentence[0]
    else:
        a = None
    return (l, a)
