#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    result = []

    for row_list in matrix:
        result.append(list(map(lambda num: num * num, row_list)))

    return result
