#!/usr/bin/python3
"""Manual test for Square class."""

from models.square import Square

# Test Square instantiation and __str__()
s1 = Square(4, 2, 1, 12)
print(s1)  # Should print: [Square] (12) 2/1 - 4

# Test display method
print("Display the square:")
s1.display()

# Test invalid size
try:
    s2 = Square(-5)
except ValueError as e:
    print(f"[{type(e).__name__}] {e}")  # Expected ValueError for negative size

# Test area method
s3 = Square(5)
print(f"Area of square: {s3.area()}")  # Should print: 25
