#!/usr/bin/python3
"""
Module that defines a function to convert a JSON string back to a Python object.
"""

import json

def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.

    Args:
        my_str (str): The JSON string to be deserialized.
    Returns:
        Any: The Python object represented by the JSON string.
    """
    return json.loads(my_str)
