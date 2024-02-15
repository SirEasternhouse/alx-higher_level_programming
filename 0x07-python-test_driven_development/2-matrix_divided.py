#!/usr/bin/python3
def matrix_divided(matrix, div):
    """ Divide all elements in a matrix.
        Args:
            param1: a matix consisting of a list of lists
            param2: the divisor

        Return:
            a divided matrix
    """
    if not isinstance(matrix, list) or \
            not all(isinstance(row, list) for row in matrix) or \
       not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_size = len(matrix[0])

    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    divided_matrix = [[round(num / div, 2) for num in row] for row in matrix]
    return divided_matrix
