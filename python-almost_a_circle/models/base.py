#!/usr/bin/python3
"""Base class module: Manages the id attribute and serialization."""
import json

class Base:
    """Base class for all other classes in this project."""
    
    __nb_objects = 0  # Private class attribute to count instances
    
    def __init__(self, id=None):
        """Initialize the Base class.
        
        Args:
            id (int): The ID for the instance, if provided. Otherwise, auto-increment.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a list of dictionaries to a JSON string."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves a list of objects to a file in JSON format."""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Converts a JSON string back to a list."""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance from a dictionary of attributes."""
        dummy = cls(1, 1)  # Dummy instance for Rectangle or Square
        dummy.update(**dictionary)
        return dummy
