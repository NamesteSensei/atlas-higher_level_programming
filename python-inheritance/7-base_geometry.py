#!/usr/bin/python3
"""
This module defines the BaseGeometry class with methods for area and integer validation.
"""

class BaseGeometry:
    """
    A class BaseGeometry with an area method and integer validation.
    """

    def area(self):
        """
        Raises an Exception indicating that the area method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that the value is an integer and greater than 0.

        Args:
            name (str): The name of the variable.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer or if value is a boolean.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) == bool or not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
