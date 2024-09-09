#!/usr/bin/python3
"""
Module for Square class.
This module provides a simple implementation of a Square
with a private size attribute.
"""


class Square:
    """Represents a square with a private instance attribute 'size'."""

    def __init__(self, size):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the square.
        """
        self.__size = size  # Private instance attribute '__size'
