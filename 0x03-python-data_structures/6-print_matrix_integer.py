#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    c = 0
    for i in range(len(matrix)):
        for j in matrix[i]:
            if (c == (len(matrix[i]) - 1)):
                print("{:d}".format(j), end = "")
            else:
                print("{:d}".format(j), end = " ")
            c += 1
        c = 0
        print("\n", end = "")
