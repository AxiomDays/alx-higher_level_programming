#!/usr/bin/python3
def matrix_divided(matrix, div):
    nutrix=[]
    bufftrix=[]
    firstlen=len(matrix[0])
    for i in matrix:
        if type(i) is not list:
            print("matrix check")
            raise TypeError ("matrix must be a matrix (list of lists) of integers/floats")
        if len(i) is not firstlen:
            raise TypeError ("Each row of the matrix must have the same size")
        for j in i:
            if type(j) is not int and type(j) is not float:
                print("{} and {}".format(j, type(j)))
                print("deepcheck")
                raise TypeError ("matrix must be a matrix (list of lists) of integers/floats")
        if type(div) is not int and type(div) is not float:
            raise TypeError ("div must be a number")
        if div == 0:
            raise ZeroDivisionError ("division by zero")
    for k in matrix:
        bufftrix=[]
        for m in k:
            m=m/div
            l=round(m,2)
            bufftrix.append(l)
        nutrix.append(bufftrix)
    return nutrix
        


