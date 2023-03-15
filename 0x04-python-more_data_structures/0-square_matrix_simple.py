#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    count, count_sub = 0, 0
    while (count < len(matrix)):
        new_matrix.append(matrix[count])
        count += 1
    count = 0
    while (count < len(new_matrix)):
        while (count_sub < 3):
            new_matrix[count][count_sub] = (matrix[count][count_sub]) ** 2
            count_sub += 1
        count += 1
    return (new_matrix)
