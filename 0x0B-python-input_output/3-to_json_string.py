#!/usr/bin/python3
"""Definition of the function to_json_string()"""
import json


def to_json_string(my_obj):
    """return the JSON representation of an object

    Args:
        my_obj: object to convert into JSON
    """
    return json.dumps(my_obj)
