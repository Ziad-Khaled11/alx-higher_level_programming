#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        j = 0
        newlist = []
        for i in my_list:
            newlist.insert(j, i)
            j += 1
        newlist[idx] = element
        return newlist
