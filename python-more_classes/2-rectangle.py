#!/usr/bin/python3
# File: 2-rectangle.py

class Rectangle:
    """
    A class to define a rectangle by its width and height
    """

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle with optional width and height parameters
        """
        # Use property setters to apply validation during initialization
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method for width
        Returns:
            int: width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for width with validation
        Args:
            value (int): The width of the rectangle
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for height
        Returns:
            int: height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for height with validation
        Args:
            value (int): The height of the rectangle
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Public method to calculate the area of the rectangle
        Returns:
            int: the area of the rectangle (width * height)
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Public method to calculate the perimeter of the rectangle
        Returns:
            int: the perimeter of the rectangle (2 * (width + height))
            or 0 if width or height is 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
