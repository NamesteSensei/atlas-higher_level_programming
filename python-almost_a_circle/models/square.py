#!/usr/bin/python3
"""Square class that inherits from Rectangle."""

from models.rectangle import Rectangle

class Square(Rectangle):
    """Represents a square, inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square instance."""
        super().__init__(size, size, x, y, id)
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size <= 0:
            raise ValueError("size must be > 0")

    def to_dictionary(self):
        """Returns the dictionary representation of a Square."""
        return {
            'id': self.id,
            'size': self.width,  # Square uses width for size
            'x': self.x,
            'y': self.y
        }

    def update(self, *args, **kwargs):
        """Assigns attributes via args or kwargs."""
        attributes = ['id', 'size', 'x', 'y']
        if args:
            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)
