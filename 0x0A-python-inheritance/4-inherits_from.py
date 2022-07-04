#!/usr/bin/python3
"""Definition of the function inherits_from()"""


def inherits_from(obj, a_class):
    """Returns True if the object is an instance of a class that inherited
    (directly or indirectly) of the specified class; otherwise False

    Args:
        obj: object to operate on
        a_class: class on which the object will be checked
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
