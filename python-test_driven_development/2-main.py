#!/usr/bin/python3
matrix_divided = __import__('1-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix_divided(matrix, 1))

try:
    print(matrix_divided(matrix, 0))  # Should raise ZeroDivisionError
except Exception as e:
    print(e)
