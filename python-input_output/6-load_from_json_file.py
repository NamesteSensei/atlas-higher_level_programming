#!/usr/bin/python3
import json

"""
Module that defines a function to load an object from a JSON file.
"""

def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename: The name of the file to load the JSON object from.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
