#!/usr/bin/python3
"""Definition of the function is_same_class()"""


def is_same_class(obj, a_class):
    """Returns True if the obj is exactly an instance of the class a_class

    Args:
        obj: object to operate on
        a_class: class on which the object will be checked
    """
    return type(obj) == a_class
