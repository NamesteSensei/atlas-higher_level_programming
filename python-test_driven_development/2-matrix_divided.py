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
    """
    # Check if matrix is a list of lists containing integers or floats
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check if each element in matrix is a number (int or float)
    for row in matrix:
        if not all(isinstance(num, (int, float)) for num in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if all rows have the same size
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    # Check if div is a number (int or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    # Check for division by zero
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Perform the division and round each result to 2 decimal places
    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]
    
    return new_matrix
