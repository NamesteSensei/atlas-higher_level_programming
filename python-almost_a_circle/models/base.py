#!/usr/bin/python3
"""Base class module: Manages id attribute for all derived classes."""
class Base:
    """Base class for all other classes in this project."""

    __nb_objects = 0  # Private class attribute to keep track of number of objects

    def __init__(self, id=None):
        """Initialize the Base class with optional id.
        
        Args:
            id (int): If provided, assign the id to the instance. Otherwise, auto-increment.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
