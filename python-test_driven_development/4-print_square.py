#!/usr/bin/python3
"""
Module to print a square using the character #
"""

def print_square(size):
    """
    Function that prints a square with the character #
    Arguments:
    size -- the size length of the square (must be an integer >= 0)
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for _ in range(size):
        print("#" * size)
