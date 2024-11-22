#!/usr/bin/python3
"""
This module contains the function `print_square(size)`.

The `print_square` function prints a square of a given size using the '#' character.
The function raises a `TypeError` if the size is not an integer and a `ValueError`
if the size is negative.
"""

def print_square(size):
    """
    Prints a square with the character '#'.
    
    Args:
    size (int): The size length of the square.
    
    Raises:
    TypeError: If size is not an integer.
    ValueError: If size is less than 0.
    """
    # Check if size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    
    # Check if size is non-negative
    if size < 0:
        raise ValueError("size must be >= 0")
    
    # Print the square of '#' characters
    for i in range(size):
        print("#" * size)
