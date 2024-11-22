#!/usr/bin/python3
def best_score(a_dictionary):
    """
    Returns the key with the largest integer value in a dictionary.
    If no score found, return None.
    """
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
