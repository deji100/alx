"""Defines a matrix_divided function that divides
   all elements of a matrix
   with parameter matrix and div, then it
   returns a new matrix
"""


def matrix_divided(matrix, div):
    """ Divides a matrix and returns a new matrix

        Args:
            matrix: a matrix containing elements
            div: value to divide matrix elements

        Returns a new matrix
    """

    if type(matrix) is list and not all([type(i) in [int, float] for x in matrix for i in x]):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    elif not all([len(x) == len(matrix[0]) for x in matrix]):
        raise TypeError("Each row of the matrix must have the same size")
    elif not type(div) in [int, float]:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        return [[round(y/div, 2) for y in z] for z in matrix]