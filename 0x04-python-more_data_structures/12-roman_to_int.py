#!/usr/bin/python3
from functools import reduce
from sre_compile import isstring


def roman_to_int(roman_string):
    roman_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
    }
    c = 0

    if (not isstring(roman_string)) or roman_string is None:
        return 0

    nbrs = [roman_int[i] for i in roman_string if i in list(roman_int.keys())]

    c = reduce(lambda a, b: -1 * (a - b) if a < b else a + b, nbrs)

    return c
