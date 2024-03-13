#!/usr/bin/python3
"""
Function Writes
"""


def write_file(filename="", text=""):
    """
    Writes in a file
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
