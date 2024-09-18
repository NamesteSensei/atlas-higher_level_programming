#!/usr/bin/python3
import json

"""
Module that defines a function to save an object to a file in JSON format.
"""

def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using JSON representation.
    
    Args:
        my_obj: The Python object to be serialized.
        filename: The name of the file where the object will be saved.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
