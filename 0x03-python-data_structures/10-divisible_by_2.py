#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        new_list = []
        j = 0
        for i in my_list:
            if i % 2 == 0:
                new_list.insert(j, True)
            else:
                new_list.insert(j, False)
            j += 1
        return new_list
