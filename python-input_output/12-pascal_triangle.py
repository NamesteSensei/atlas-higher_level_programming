#!/usr/bin/python3
"""
Module that defines a function to generate Pascal's triangle.
"""

def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row.
    
    Args:
        n (int): The number of rows.
    
    Returns:
        list of lists: Pascal's triangle up to the nth row.
    """
    if n <= 0:
        return []
    
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
        return triangle
