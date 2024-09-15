#!/usr/bin/python3
"""
This module defines a Rectangle class that tracks the number of instances and
uses a customizable symbol for its string representation.
"""


class Rectangle:
    """
    A class used to represent a Rectangle.
    
    Attributes
    ----------
    number_of_instances : int
        Class attribute that tracks the number of Rectangle instances.
    print_symbol : any
        Class attribute that defines the symbol used for string representation.
    width : int
        The width of the rectangle, must be a non-negative integer.
    height : int
        The height of the rectangle, must be a non-negative integer.
    
    Methods
    -------
    area():
        Returns the area of the rectangle.
    perimeter():
        Returns the perimeter of the rectangle.
    __str__():
        Provides a string representation of the rectangle using the symbol in `print_symbol`.
    __repr__():
        Provides a string representation to recreate the object using eval().
    __del__():
        Prints a message when the instance of the rectangle is deleted.
    """

    # Class attributes
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle object with optional width and height.
        Increments the number_of_instances class attribute.

        Parameters
        ----------
        width : int, optional
            The width of the rectangle (default is 0)
        height : int, optional
            The height of the rectangle (default is 0)
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1  # Increment instance count

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
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns a string representation of the rectangle using `print_symbol`."""
        if self.width == 0 or self.height == 0:
            return ""
        # Convert print_symbol to a string and use it to represent the rectangle
        symbol = str(self.print_symbol)
        return "\n".join([symbol * self.width for _ in range(self.height)])

    def __repr__(self):
        """Returns a string representation to recreate the object using eval().
        
        The format should be: Rectangle(width, height)
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Prints 'Bye rectangle...' when the instance is deleted and decrements the instance count."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1  # Decrement instance count
