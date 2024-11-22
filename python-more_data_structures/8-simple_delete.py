#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    Deletes a key in a dictionary.

    :param a_dictionary: The dictionary to delete the key from
    :param key: The key to delete
    :return: The updated dictionary
    """

    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
