# Python - More Data Structures: Set, Dictionary

This repository contains projects related to advanced data structures in Python, particularly focusing on sets, dictionaries, and other data-related tasks. The exercises are designed to provide practice with Python's built-in data structures and to improve your problem-solving skills.

## Project Overview

### 0. Squared Simple
- **File**: `0-square_matrix_simple.py`
- **Description**: 
  - This module defines a function `square_matrix_simple(matrix=[])` that computes the square value of all integers in a matrix.
  - The function returns a new matrix of the same size as the input matrix, with each value squared.
  - The original matrix is not modified.

### Example Usage

```python
#!/usr/bin/python3
square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)
