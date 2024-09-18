#!/usr/bin/python3
import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Load existing items from the file if it exists
if os.path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Add new arguments from the command line
my_list.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(my_list, filename)
