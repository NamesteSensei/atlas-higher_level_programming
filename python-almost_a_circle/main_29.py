#!/usr/bin/python3
"""Manual test for Rectangle display method."""

from models.rectangle import Rectangle

r1 = Rectangle(4, 6)
print("Rectangle with no x and y:")
r1.display()

r2 = Rectangle(2, 3, 2, 2)
print("\nRectangle with x=2 and y=2:")
r2.display()
