#!/usr/bin/python3
"""
Function that reads
"""


def read_file(filename=""):
    """
    Function Reads from a file
    """
    with open(filename, "r") as f:
        line = f.readline()
        while line:
            print(line.strip())
            line = f.readline()
