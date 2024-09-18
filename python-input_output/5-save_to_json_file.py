#!/usr/bin/python3
"""
This module contains a function that writes an object to a text file
using JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using JSON representation.

    Args:
        my_obj: The object to serialize.
        filename: The name of the file to write the object to.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
