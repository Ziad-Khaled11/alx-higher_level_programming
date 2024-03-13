#!/usr/bin/python3
"""
Function that reads
"""


def read_file(filename=""):
    """
    Function Reads from a file
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
