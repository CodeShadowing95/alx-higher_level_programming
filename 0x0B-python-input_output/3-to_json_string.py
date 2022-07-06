#!/usr/bin/python3
import json


"""Definition of the function to_json_string()"""


def to_json_string(my_obj):
    """return the JSON representation of an object

    Args:
        my_obj: object to convert into JSON
    """
    return json.dumps(my_obj)
