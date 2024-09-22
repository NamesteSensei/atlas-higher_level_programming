#!/usr/bin/python3
"""Rectangle class module: Inherits from Base."""

from models.base import Base

class Rectangle(Base):
    """Represents a rectangle, inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle instance."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Print the Rectangle using the `#` character."""
        for i in range(self.height):
            print("#" * self.width)
