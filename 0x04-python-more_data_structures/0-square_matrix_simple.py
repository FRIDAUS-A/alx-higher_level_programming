#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    count = 0
    new_matrix = []
    while (count < len(matrix)):
        tmp_matrix = list(map(lambda x: x ** 2, matrix[count]))
        count += 1
        new_matrix.append(tmp_matrix)
    return (new_matrix)
