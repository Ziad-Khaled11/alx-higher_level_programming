#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    copied = []
    for x in range(len(matrix)):
        temp = []
        for elem in matrix[x]:
            temp.append(elem ** 2)
        copied.append(temp)
    return copied
