#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_set = set(my_list)
    sum = 0
    for i in new_set:
        sum += i
    return sum
