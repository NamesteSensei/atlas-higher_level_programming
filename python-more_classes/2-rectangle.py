#!/usr/bin/python3
# File: 2-rectangle.py

class Rectangle:
    """
    A class to define a rectangle by its width and height.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    
    Methods:
        __init__(self, width, height): Initializes the rectangle.
        area(self): Returns the area of the rectangle.
        perimeter(self): Returns the perimeter of the rectangle.
    """
    
    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle with optional width and height parameters.
        
        Args:
            width (int): Width of the rectangle (default: 0).
            height (int): Height of the rectangle (default: 0).
        """
        self.width = width  # Initialize width using the property setter.
        self.height = height  # Initialize height using the property setter.

    @property
    def width(self):
        """
        Getter method for the width.
        
        Returns:
            int: The current width of the rectangle.
        """
        return self.__width  # Return the private attribute __width.

    @width.setter
    def width(self, value):
        """
        Setter method for the width with validation.
        
        Args:
            value (int): The width value to set.
        
        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")  # Check if width is an integer.
        if value < 0:
            raise ValueError("width must be >= 0")  # Ensure width is non-negative.
        self.__width = value  # Set the private attribute __width.

    @property
    def height(self):
        """
        Getter method for the height.
        
        Returns:
            int: The current height of the rectangle.
        """
        return self.__height  # Return the private attribute __height.

    @height.setter
    def height(self, value):
        """
        Setter method for the height with validation.
        
        Args:
            value (int): The height value to set.
        
        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")  # Check if height is an integer.
        if value < 0:
            raise ValueError("height must be >= 0")  # Ensure height is non-negative.
        self.__height = value  # Set the private attribute __height.

    def area(self):
        """
        Public method to calculate the area of the rectangle.
        
        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.__width * self.__height  # Calculate area (width * height).

    def perimeter(self):
        """
        Public method to calculate the perimeter of the rectangle.
        
        Returns:
            int: The perimeter of the rectangle (2 * (width + height)).
                  If width or height is 0, returns 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0  # If either width or height is 0, perimeter is 0.
        return 2 * (self.__width + self.__height)  # Calculate perimeter.

