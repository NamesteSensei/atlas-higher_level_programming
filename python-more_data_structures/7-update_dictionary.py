#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds key/value in a dictionary.

    :param a_dictionary: The dictionary to update
    :param key: The key to update/add
    :param value: The value to set for the key
    :return: The updated dictionary
    """
    a_dictionary[key] = value
    return a_dictionary
