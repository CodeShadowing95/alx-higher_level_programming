#!/usr/bin/python3
"""
doctest_add_integer.py
This module supplies the function add_integer().
Raises: TypeError if a or b are not integer or float
"""


def add_integer(a, b=98):
    """
    Return the result of a + b
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
