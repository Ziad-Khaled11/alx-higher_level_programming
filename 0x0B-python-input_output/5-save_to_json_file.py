#!/usr/bin/python3
"""
writes in json file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    save to json file
    """
    json_st = json.dump(my_obj)
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(json_st)
