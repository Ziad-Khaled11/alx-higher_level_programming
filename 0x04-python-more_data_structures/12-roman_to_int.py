#!/usr/bin/python3
def roman_to_int(roman_string):
    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if roman_string and isinstance(roman_string, str):
        Sum = 0
        for i in roman_string:
            for key, value in dic.items():
                if i == key:
                    Sum += value
        return Sum
    else:
        return 0
