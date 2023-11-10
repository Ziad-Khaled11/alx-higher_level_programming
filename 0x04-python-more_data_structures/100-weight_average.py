#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        Sum = 0
        quot = 0
        for i in my_list:
            Sum += i[0] * i[1]
            quot += i[1]
        averge = Sum / quot
        return averge
