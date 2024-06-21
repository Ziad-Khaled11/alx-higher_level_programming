#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        length = len(my_list)
        length *= -1
        i = -1
        while i >= length:
            print("{:d}".format(my_list[i]))
            i -= 1
