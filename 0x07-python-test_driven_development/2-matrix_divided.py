#!/usr/bin/python3
"""
doctest_matrix_divided.py

This module supplies the function matrix_divided()

>>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
"""


def matrix_divided(matrix, div):
    """Return a new matrix

    Params:
        matrix: list of lists of integers or floats
        div: number (int or float)

    Raises:
        TypeError if matrix is not a list of lists of integers or floats
        TypeError if each row of the matrix is not of the same size
        TypeError if div is not a number (int or float)
        ZeroDivisionError if div is 0
    """
    e1 = 'matrix must be a matrix (list of lists) of integers/floats'
    e2 = 'Each row of the matrix must have the same size'
    e3 = 'div must be a number'
    e4 = 'division by zero'
    if isinstance(matrix, list):
        if all(isinstance(tab, list) for tab in matrix):
            if len(set(map(len, matrix))) == 1:
                check_int = all(type(j) != int for i in matrix for j in i)
                check_float = all(type(b) != float for a in matrix for b in a)
                if not check_int and (not check_float):
                    raise TypeError(e1)
            else:
                raise TypeError(e2)
        else:
            raise TypeError(e1)
    else:
        raise TypeError(e1)

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError(e3)
    elif div == 0:
        raise ZeroDivisionError(e4)

    return [[float("{0:.2f}".format(n / div)) for n in tab] for tab in matrix]
