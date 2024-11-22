#!/usr/bin/python3
"""
This module contains a function that loads an object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Loads an object from a JSON file.

    Args:
        filename: The name of the JSON file to load the object from.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
