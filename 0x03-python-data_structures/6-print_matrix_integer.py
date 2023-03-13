#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for mem in matrix:
        for mem_1 in mem:
            print("{:d}".format(mem_1), end="")
            if (mem_1 != mem[len(mem_1) - 1]):
                print(" ", end="")
            if (mem != matrix[len(mem) - 1]):
                print()
