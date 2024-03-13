#!/usr/bin/python3
"""
writes in json file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    save to json file
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
