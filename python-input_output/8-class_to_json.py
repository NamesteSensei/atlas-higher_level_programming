#!/usr/bin/python3
"""
Module that returns a dictionary description of an object for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns the dictionary description for JSON serialization of an object.

    Args:
        obj: The object instance to serialize.

    Returns:
        dict: A dictionary with all the attributes of the object.
    """
    return obj.__dict__
