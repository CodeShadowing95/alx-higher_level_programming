#!/usr/bin/python3
"""Definition of the function pascal_triangle()"""


def pascal_triangle(n):
    """returns a list of lists of integers representing the Pascal's triangle
    of n

    Args:
        n: number of lists of lists of integer
    """
    tab = []
    s = []
    j = 0
    if n <= 0:
        return []
    for i in range(n):
        if i < 1:
            temp = [1]
            tab.append(temp)
        else:
            s.append(temp[0])
            for i in range(len(temp)-1):
                j = i + 1
                if j != len(temp):
                    s.append(temp[i] + temp[j])
            s.append(temp[j])
            tab.append(s)
            temp = s
            s = []
    return tab
