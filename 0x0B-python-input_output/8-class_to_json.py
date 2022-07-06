#!/usr/bin/python3
"""Definition of the function class_to_json()"""


def class_to_json(obj):
    """returns the dictionary description for JSON serialization of an object

    Args:
        obj: instance of a class
    """
    return obj.__dict__
