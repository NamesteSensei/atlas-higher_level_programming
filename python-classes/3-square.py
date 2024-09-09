#!/usr/bin/python3
"""
This module defines a class Square with size validation and
a method to calculate the area of the square.
"""


class Square:
    """A class that defines a square."""

    def __init__(self, size=0):
        """
        Initialize a Square instance with a private size attribute.

        Args:
            size (int): The size of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size  # private instance attribute

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2