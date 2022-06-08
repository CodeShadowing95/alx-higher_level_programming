#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix2 = []

    for i in range(len(matrix)):
        matrix2.append(list(map(lambda x: x ** 2, matrix[i])))

    return matrix2
