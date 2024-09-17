#!/usr/bin/python3
"""
This module defines the MyList class which inherits from the built-in list class.
"""

class MyList(list):
    """
    MyList inherits from the built-in list class and adds a method to print the list sorted.
    """
    def print_sorted(self):
        """
        Prints the list in ascending order.
        Does not modify the original list.
        """
        # Use sorted() to create a sorted copy of the list
        print(sorted(self))  # Print the sorted list
