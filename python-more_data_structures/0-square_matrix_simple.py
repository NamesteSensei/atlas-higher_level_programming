#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Computes the square of all integers in a matrix.

    :param matrix: A 2D list of integers
    :return: A new matrix with each element squared
    """
    # Using list comprehension to create a new matrix
    return [[element ** 2 for element in row] for row in matrix]
