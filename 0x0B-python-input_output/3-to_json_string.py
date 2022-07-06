#!/usr/bin/python3
from json import dumps


"""Definition of the function to_json_string()"""


def to_json_string(my_obj):
    """return the JSON representation of an object

    Args:
        my_obj: object to convert into JSON
    """
    return dumps(my_obj)
