#!/usr/bin/python3
"""
This module defines a class Square with size validation,
getter, setter, and area calculation.
"""


class Square:
    """A class that defines a square with a private size attribute."""

    def __init__(self, size=0):
        """
        Initialize a Square instance with a private size attribute.

        Args:
            size (int): The size of the square (default is 0).
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size  # Calls the setter for validation

    @property
    def size(self):
        """Getter for the private size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the private size attribute.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:

