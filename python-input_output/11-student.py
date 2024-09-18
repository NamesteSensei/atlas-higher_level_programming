#!/usr/bin/python3
"""
Defines a Student class with serialization and deserialization methods.
"""

class Student:
    """Represents a student."""
    
    def __init__(self, first_name, last_name, age):
        """Initializes the student with first name, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        
        Args:
            attrs (list): List of attribute names that should be retrieved.
        
        Returns:
            dict: A dictionary representation of the Student instance.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        return self.__dict__
    
    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with data from a JSON dictionary.
        
        Args:
            json (dict): A dictionary representing new attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)
