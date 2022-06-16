#!/usr/bin/python3
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

    s = 0

    if (not isstring(roman_string)) or roman_string == "":
        return (0)

    romans_converted = [roman_int[roman_nbr] for roman_nbr in roman_string]

    for i in range(0, len(romans_converted)):
        s += romans_converted[i]
        if i > 0:
            if romans_converted[i] > romans_converted[i-1]:
                s -= (romans_converted[i] + romans_converted[i-1])
                s += (romans_converted[i] - romans_converted[i-1])

    if s in range(1, 4000):
        return (s)
