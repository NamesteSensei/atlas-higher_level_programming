#!/usr/bin/python3
"""
This module defines a Rectangle class that defines a rectangle by
its width and height.
"""


class Rectangle:
    """
    A class used to represent a Rectangle.
    ----------
    width : int
        The width of the rectangle, must be a non-negative integer.
    height : int
        The height of the rectangle, must be a non-negative integer.
    
    Methods
        Returns the area of the rectangle.
    perimeter():
        Returns the perimeter of the rectangle.
    __str__():
        Provides a string representation of the rectangle using '#'.
    __repr__():
        Provides a string representation in the format used for object memory addresses.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle object with optional width and height.
        Parameters
        ----------
        width : int, optional
            The width of the rectangle (default is 0)
        height : int, optional
            The height of the rectangle (default is 0)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for the width attribute."""
        return self._width

    @width.setter
    def width(self, value):
        """Setter for the width attribute with type and value checks."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Getter for the height attribute."""
        return self._height

    @height.setter
    def height(self, value):
        """Setter for the height attribute with type and value checks."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle.
        
        Returns 0 if either width or height is 0.
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns a string representation of the rectangle using '#'."""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.width for _ in range(self.height)])

    def __repr__(self):
        """Returns a string representation with module and class name.
        
        The format should be: <3-rectangle.Rectangle object at memory_address>
        """
        return f"<3-rectangle.Rectangle object at {hex(id(self))}>"

