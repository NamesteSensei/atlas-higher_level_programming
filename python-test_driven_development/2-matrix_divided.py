#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix by a number.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div, rounding to 2 decimal places.

    Args:
        matrix (list of lists): A matrix (list of lists) of integers/floats.
        div (int, float): The divisor.

    Returns:
        list of lists: A new matrix with each element divided by div.

    Raises:
        TypeError: If the matrix is not a list of lists of integers/floats,
                   if the rows are not the same size, or if div is not a number.
        ZeroDivisionError: If div is zero.
        ValueError: If the matrix contains NaN or infinity.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if not all(isinstance(num, (int, float)) for num in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        for num in row:
            if num != num or num in [float('inf'), -float('inf')]:
                raise ValueError("matrix contains NaN or infinity")

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if div != div or div in [float('inf'), -float('inf')]:
        raise ValueError("div cannot be NaN or infinity")

    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]
    
    return new_matrix
