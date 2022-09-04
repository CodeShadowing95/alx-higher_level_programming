#!/usr/bin/python3
"""
doctest_print_square

Print a square with the character #

>>> print_square(4)
####
####
####
####
"""


def print_square(size):
    """Print a square with the character # by size

    Params:
        size: (int) length of the square

    Raises:
        TypeError if size is not an integer
        ValueError if size is less than 0
        TypeError if size is a float and is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
