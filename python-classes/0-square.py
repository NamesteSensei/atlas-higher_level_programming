#!/usr/bin/python3
"""
Module for defining the Square class.
This module defines a class Square with a private size attribute.
"""


class Square:
    """
    Represents a square with a private instance attribute 'size'.
    
    Attributes:
        __size (int): The size of the square (no type/value validation).
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance with the given size.

        Args:
            size (int): The size of the square, default is 0.
        """
        self.__size = size  # Private instance attribute

