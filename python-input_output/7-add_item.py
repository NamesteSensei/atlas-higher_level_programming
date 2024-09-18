#!/usr/bin/python3
"""
This script adds all arguments to a Python list and saves them
to a file in JSON format.
"""

import sys
from os import path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Load existing data from the JSON file, or create an empty list if the file doesn't exist
if path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Add command-line arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list back to the JSON file
save_to_json_file(my_list, filename)
