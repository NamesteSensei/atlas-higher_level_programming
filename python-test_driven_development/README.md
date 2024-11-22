# Python Test-Driven Development

## Project Overview
This project demonstrates test-driven development (TDD) practices in Python by implementing functions with proper tests using `doctest`. 

The primary function implemented in this project is:
- **`add_integer(a, b=98)`**: A function that adds two integers or floats and returns their sum as an integer.

## Files
- **0-add_integer.py**: Contains the `add_integer` function which performs addition with type checking.
- **tests/0-add_integer.txt**: Includes `doctest` test cases to validate the functionality of `add_integer`.
- **README.md**: Project documentation (this file).

## Usage
- Ensure the files are executable by including the shebang (`#!/usr/bin/python3`).
- To run the doctests and verify that the function works as expected, use:
  ```bash
  python3 -m doctest -v tests/0-add_integer.txt

