#!/usr/bin/python3
"""
This module provides a function to add two integers.
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats and returns the sum as an integer.
    
    Args:
        a (int, float): The first number.
        b (int, float, optional): The second number (default is 98).
    
    Returns:
        int: The sum of a and b as an integer.
    
    Raises:
        TypeError: If a or b are not integers or floats.
        ValueError: If a or b is NaN.
        OverflowError: If a or b is too large (infinity).
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    # Check for NaN values
    if a != a or b != b:  # NaN check
        raise ValueError("cannot convert float NaN to integer")

    # Check for float overflow (infinity)
    if (a == float('inf') or b == float('inf') or
            a == -float('inf') or b == -float('inf')):
        raise OverflowError("float value too large")
    
    return int(a) + int(b)
