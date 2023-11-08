#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nu_trix = []
    buff_trix = []
    for i in range(len(matrix)):
        buff_trix = []
        for j in matrix[i]:
            j *= j
            buff_trix.append(j)
        nu_trix.append(buff_trix)
    return nu_trix



