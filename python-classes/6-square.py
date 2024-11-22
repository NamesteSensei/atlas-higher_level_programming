#!/usr/bin/python3
"""
This module defines a class Square with size and position validation,
and the ability to print the square at a specified position.
"""


class Square:
    """A class that defines a square with a private size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a Square instance with private size and position attributes.

        Args:
            size (int): The size of the square (default is 0).
            position (tuple): The position to print the square
                              (default is (0, 0)).

        Raises:
            TypeError: If size is not an integer or position is not a tuple
                       of 2 positive integers.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

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
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for the private position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for the private position attribute.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the # character.

        If size is 0, it prints an empty line.
        The square is printed at the position specified by the `position`
        attribute.
        """
        if self.__size == 0:
            print("")
            return

        # Print new lines for the vertical offset (position[1])
        [print("") for _ in range(self.__position[1])]

        # Print each row of the square with horizontal offset (position[0])
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
