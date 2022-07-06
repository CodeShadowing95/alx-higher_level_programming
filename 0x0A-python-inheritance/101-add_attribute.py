#!/usr/bin/python3
"""definition of the function add_attribute()"""


def add_attribute(obj, attibute, value):
    """function add_attribute

    Args:
        obj: object's name in which attributes will be set
        name: name of the attibute of that object that we want to assign value
        value: the attibute value

    Raises:
        TypeError if cannot add attribute
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, attibute, value)
    else:
        raise TypeError("can't add new attibute")
