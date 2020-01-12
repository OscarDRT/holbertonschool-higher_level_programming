#!/usr/bin/python3
def matrix_divided(matrix, div):
    msn1 = "matrix must be a matrix (list of lists) of integers/floats"
    msn2 = "Each row of the matrix must have the same size"
    msn3 = "div must be a number"
    msn4 = "division by zero"
    if type(matrix) != list:
        raise TypeError(msn1)
    else:
        for i in range(len(matrix)):
            if type(matrix[i]) != list:
                raise TypeError(msn1)
            leng = len(matrix[0])
            if len(matrix[i]) != leng:
                raise TypeError(msn2)
            for j in range(len(matrix[i])):
                if type(matrix[i][j]) != int and type(matrix[i][j]) != float:
                    raise TypeError(msn1)
    if type(div) != int and type(div) != float:
        raise TypeError(msn3)
    elif div == 0:
        raise ZeroDivisionError(msn4)
    else:
        return list(map(lambda i: list(map(lambda j: round(j / div, 2), i)), matrix))


