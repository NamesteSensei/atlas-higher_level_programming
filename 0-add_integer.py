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
    """
    # Check if 'a' is either an int or a float
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    
    # Check if 'b' is either an int or a float
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    # Cast both 'a' and 'b' to integers if they are floats
    a = int(a)
    b = int(b)
    
    return a + b
