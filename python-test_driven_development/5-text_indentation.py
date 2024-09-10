#!/usr/bin/python3
"""
This module contains the function `text_indentation(text)`.

The `text_indentation` function prints a text with 2 new lines after each of
the following characters: '.', '?', and ':'.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: '.', '?', and ':'.
    
    Args:
    text (str): The text to be printed.
    
    Raises:
    TypeError: If the input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        # Print the current character
        print(text[i], end="")
        
        # If a punctuation mark is found, print two new lines
        if text[i] in ".?:":
            print("\n")
            # Skip spaces after the punctuation mark
            while i + 1 < len(text) and text[i + 1] == " ":
                i += 1
        i += 1
