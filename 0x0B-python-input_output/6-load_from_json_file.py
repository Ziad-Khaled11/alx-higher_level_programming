#!/usr/bin/python3
"""
Loads from json file
"""
import json


def load_from_json_file(filename):
    """
    creates an Object from a “JSON file”
    """
    with open(filename, 'r', encoding="utf-8") as f:
        loaded = json.load(f)
    return loaded
