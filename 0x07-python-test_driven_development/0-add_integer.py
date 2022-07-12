#!/usr/bin/python3
"""doctest_add_integer.py

>>> add_integer(2, 9)
11
"""


def add_integer(a, b=98):
    """Function that adds two integers

    Args:
        a: integer
        b: integer

    Raises:
        TypeError if a and b are not integer or float
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
