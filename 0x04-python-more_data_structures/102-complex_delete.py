#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = []
    for key, values in a_dictionary.items():
        if values == value:
            keys.append(key)
    if keys:
        for i in keys:
            a_dictionary.pop(i)
    return a_dictionary
