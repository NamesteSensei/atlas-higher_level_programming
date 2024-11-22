#!/usr/bin/python3
"""Manual testing for the Square class."""

from models.square import Square

# Create a Square instance
s = Square(5)
print(f"Square: {s}")

# Test area calculation
print(f"Area of Square: {s.area()}")

# Test update method with args
s.update(89, 10)
print(f"Updated Square (id, size): {s}")

# Test to_dictionary method
print(f"Dictionary representation of Square: {s.to_dictionary()}")

# Test display method
print("Display the Square:")
s.display()
