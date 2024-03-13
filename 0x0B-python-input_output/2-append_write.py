#!/usr/bin/python3
"""
Function appends
"""


def append_write(filename="", text=""):
    """
    appends a given text in a file
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
