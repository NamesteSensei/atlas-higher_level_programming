 #!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    This function returns a new matrix where each element is the square
    of the corresponding element in the original matrix.
    """
    # Using a list comprehension to create a new matrix with squared values
    new_matrix = [[element ** 2 for element in row] for row in matrix]
    
    return new_matrix  # Return the newly created matrix
