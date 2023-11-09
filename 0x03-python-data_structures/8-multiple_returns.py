#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        length = len(sentence)
        char = sentence[0]
    else:
        length = 0
        char = None
    return length, char
