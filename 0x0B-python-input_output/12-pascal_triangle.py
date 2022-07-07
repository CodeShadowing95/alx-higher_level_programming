#!/usr/bin/python3
"""Definition of the function pascal_triangle()"""


def pascal_triangle(n):
    """returns a list of lists of integers representing the Pascal's triangle
    of n

    Args:
        n: number of lists of lists of integer
    """
    if n <= 0:
        return []
    for i in range(n):
        
