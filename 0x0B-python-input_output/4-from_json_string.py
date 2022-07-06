#!/usr/bin/python3
"""Definition of the function from_json_string()"""
import json


def from_json_string(my_str):
    """returns an object represented by a JSON string

    Args:
        my_str: string to operate on
    """
    return json.loads(my_str)
