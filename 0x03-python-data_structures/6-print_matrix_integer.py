#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        cols = len(matrix[0])
        for row in matrix:
            i = 0
            for element in row:
                if i != cols - 1:
                    print("{}".format(element), end=" ")
                else:
                    print("{}".format(element), end="")
                i += 1
            print()
