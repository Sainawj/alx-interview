#!/usr/bin/python3
"""
Rotate 2D Matrix
This script rotates a 2D matrix 90 degrees clockwise in place.
"""


def rotate_2d_matrix(matrix):
    """Rotate two dimension matrix 90 degrees clockwise.
    
    Args:
        matrix (list[[list]]): A square matrix (list of lists).
    """
    n = len(matrix)  # Get the size of the matrix (assuming it's square)
    for i in range(int(n / 2)):  # Loop over the first half of the rows
        y = (n - i - 1)  # Calculate the corresponding column
        for j in range(i, y):  # Loop through each element in the layer
            x = (n - 1 - j)  # Calculate the corresponding row index
            # Store the current element to be rotated
            tmp = matrix[i][j]
            # Move the value from the left to the top
            matrix[i][j] = matrix[x][i]
            # Move the value from the bottom to the left
            matrix[x][i] = matrix[y][x]
            # Move the value from the right to the bottom
            matrix[y][x] = matrix[j][y]
            # Move the value from the top to the right
            matrix[j][y] = tmp
