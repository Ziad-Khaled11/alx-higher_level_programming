#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    last = number % 10
elif number < 0:
    last = number % -10
else:
    last = 0
if last == 0:
    print("Last digit of {} is {} and is {}".format(number, last, last))
elif last > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, last))
else:
    print(f"Last digit of {number} is {last} and is less than 6 and not 0")