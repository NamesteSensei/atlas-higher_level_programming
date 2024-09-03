# Python Exceptions Project

This project focuses on handling exceptions in Python using the `try`, `except`, and `finally` blocks. The goal is to correctly manage errors and exceptions in a Python program without crashing the application, ensuring robust and error-free code execution.

## Project Requirements

- Python version: 3.8.5 (Ubuntu 20.04 LTS)
- All files are executable.
- PEP 8 style guide compliance (`pycodestyle` version 2.7.*).
- No external libraries or modules are allowed.
- Each file ends with a new line.
- Each file starts with the shebang `#!/usr/bin/python3`.

## Tasks

### 0. Safe List Printing
- **File**: `0-safe_print_list.py`
- Function that prints `x` elements of a list and returns the number of elements printed.

### 1. Safe Printing of an Integer
- **File**: `1-safe_print_integer.py`
- Function that safely prints an integer using `{:d}.format()`.

### 2. Print and Count Integers
- **File**: `2-safe_print_list_integers.py`
- Function that prints the first `x` elements of a list and only integers, returning the count of integers printed.

### 3. Integers Division with Debug
- **File**: `3-safe_print_division.py`
- Function that divides two integers and prints the result, handling division errors gracefully.

### 4. Divide a List
- **File**: `4-list_division.py`
- Function that divides element by element two lists and returns a new list, handling errors like division by zero, wrong types, or out-of-range errors.

### 5. Raise Exception
- **File**: `5-raise_exception.py`
- Function that raises a `TypeError` exception.

### 6. Raise a Message
- **File**: `6-raise_exception_msg.py`
- Function that raises a `NameError` with a custom message.

## Usage

To run the programs, simply execute the corresponding main file. For example:

```bash
./0-main.py

