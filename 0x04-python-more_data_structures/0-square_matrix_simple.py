#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Iterate through each row of the input matrix
    for i in range(len(matrix)):
        # Apply the square operation to each value in the current row
        matrix[i] = [value ** 2 for value in matrix[i]]

    return( matrix)
