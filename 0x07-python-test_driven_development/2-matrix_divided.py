#!/usr/bin/python3

"""A FUNCTION THAT DIVIDES ALL ELEMENTS OF A MATRIX"""

def matrix_divided(matrix, div):
    """A function that divides a matrix by a value div
        Args:
            matrix (list[list]): maatrix
            div (float or int): 
    """
    if (type(matrix) is not list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    else:
        for index_value in matrix:
            if (type(index_value) is not list):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            else:
                for mem in index_value:
                    if (type(mem) != float and type(mem) != int):
                        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for index_value in matrix:
            if (len(matrix[1]) is not len(index_value)):
                raise TypeError("Each row of the matrix must have the same size")
    if (type(div) != float and type(div) != int):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    
    new_matrix = []
    for index_value in matrix:
        value = []
        for mem in index_value:
            value.append(mem)
        new_matrix.append(value)
    for index_value in new_matrix:
        index = len(index_value) - 1
        while (index >= 0):
            index_value[index] /= div
            index_value[index] = float("{:.2f}".format(index_value[index]))
            index = index - 1
    return (new_matrix)
