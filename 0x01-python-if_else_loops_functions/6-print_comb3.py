#!/usr/bin/python3
for i in range(1, 99):
    if i % 10 <= int(i / 10):
        continue
    if i != 89:
        print("{:02d}, ".format(i), end="")
    else:
        print("{:02d}".format(i))
