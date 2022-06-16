#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    if len(matrix) == 0:
        return (0)
    tab = list(
            map(
                lambda x: x, map(
                    lambda x: [x[0]**2, x[1]**2, x[2]**2], matrix)))

    return (tab)
