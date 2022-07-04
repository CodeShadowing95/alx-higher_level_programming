#!/usr/bin/python3
"""Definition of the function is_kind_of_class()"""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance of, or if the object is
    an instance of a class that inherited from, the specified class;
    otherwise False

    Args:
        obj: object to operate on
        a_class: class on which the object will be checked
    """
    return isinstance(obj, a_class)
