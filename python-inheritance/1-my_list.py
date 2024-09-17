#!/usr/bin/python3
"""
Module MyList
Defines a class MyList that inherits from list.
"""

class MyList(list):
    """
    MyList is a subclass of list with an additional method to print the list in sorted order.
    """
    
    def print_sorted(self):
        """
        Prints the list in ascending order.
        It does not modify the original list.
        """
        # Sort the list and print the sorted version
        sorted_list = sorted(self)
        print(sorted_list)
