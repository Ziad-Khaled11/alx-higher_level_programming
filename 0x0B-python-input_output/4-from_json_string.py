#!/usr/bin/python3
"""
deserialize a json string
"""
import json


def from_json_string(my_str):
    """
    returns object
    """
    return json.loads(my_str)
