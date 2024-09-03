#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Replaces all occurrences of search with replace in a new list.

    :param my_list: The original list
    :param search: The element to search for in the list
    :param replace: The element to replace search with in the new list
    :return: A new list with the replaced elements
    """
    # Creating a new list using list comprehension
    return [replace if element == search else element for element in my_list]
