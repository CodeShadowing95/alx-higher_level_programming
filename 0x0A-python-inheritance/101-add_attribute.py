#!/usr/bin/python3
"""definition of the function add_attribute()"""


def add_attribute(obj, name, value):
    """function add_attribute
    Args:
        obj: object's name in which attributes will be set
        name: name of the attibute of that object that we want to assign value
        value: the attibute value
    """
    types = [int, bool, float, complex, str, list, tuple, set, dict, None:]
    if type(obj) in types:
        raise TypeError("can't add new attibute")
    else:
        setattr(obj, name, value)
