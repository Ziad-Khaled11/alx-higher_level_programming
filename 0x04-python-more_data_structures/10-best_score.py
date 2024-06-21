#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        maximum = -10000
        for key, value in a_dictionary.items():
            if value > maximum:
                maximum = value
                Key = key
        return Key
    else:
        return None
