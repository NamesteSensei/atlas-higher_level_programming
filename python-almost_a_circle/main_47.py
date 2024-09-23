#!/usr/bin/python3
"""Manual test for Rectangle save_to_file with None."""

from models.rectangle import Rectangle

# Test save_to_file with None
Rectangle.save_to_file(None)

# Read and print the content of the file to verify it saved "[]"
with open("Rectangle.json", "r") as file:
    print(file.read())  # Expected output: []
