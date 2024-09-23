#!/usr/bin/python3
"""Manual test for Rectangle.save_to_file(None)."""

from models.rectangle import Rectangle

# Call save_to_file with None
Rectangle.save_to_file(None)

# Open the file and print its contents to verify the result
with open("Rectangle.json", "r") as file:
    content = file.read()
    print(content)  # Expected output: []
