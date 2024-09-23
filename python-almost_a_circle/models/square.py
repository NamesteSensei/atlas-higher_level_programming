#!/usr/bin/python3
"""Square class that inherits from Rectangle."""

from models.rectangle import Rectangle

class Square(Rectangle):
    """Represents a square, inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square instance."""
        super().__init__(size, size, x, y, id)
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size <= 0:
            raise ValueError("size must be > 0")

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square, updating both width and height."""
        self.width = value
        self.height = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.width * self.height

    def display(self):
        """Print the Square using the `#` character."""
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return a string representation of the square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def to_dictionary(self):
        """Returns the dictionary representation of a Square."""
        return {
            'id': self.id,
            'size': self.width,
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
