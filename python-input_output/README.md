Python Input/Output Project

Description
This project demonstrates file input and output operations in Python. The tasks cover reading, writing, and appending to text files using Python’s built-in functions. Each function follows best practices like using the with statement to handle files safely and cleanly.

Requirements
Python 3.8.5 on Ubuntu 20.04 LTS
All Python files must adhere to PEP8 standards (pycodestyle 2.7.*).
Files should be executable and end with a new line.
Project Structure
0-read_file.py: A function that reads a text file and prints its contents to stdout.
1-write_file.py: A function that writes a string to a text file and returns the number of characters written.
2-append_write.py: A function that appends a string to a text file and returns the number of characters added.
tests/: Contains test cases for validating each function using doctests.
Usage
Run Python Scripts:

bash
Copy code
./0-main.py   # Test read_file function
./1-main.py   # Test write_file function
./2-main.py   # Test append_write function
Run Doctests: Validate the functions by running doctests:

bash
Copy code
python3 -m doctest ./tests/*
