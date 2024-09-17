#!/usr/bin/python3
"""
This module defines a Square class that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    A class representing a square, inherited from Rectangle.
    """

    def __init__(self, size):
        """
        Initialize a square with a given size.

        Args:
            size (int): The size of the square's sides.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Returns the area of the square.

        Returns:
            The area of the square (int).
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns a string representation of the square.
        """
        return f"[Square] {self.__size}/{self.__size}"
