#!/usr/bin/python3
"""
Function to calculate the perimeter of an island described in a grid.
The grid is a rectangular matrix of 1s (land) and 0s (water).
"""


def island_perimeter(grid):
    """
    Function to calculate the perimeter of the island in the grid.

    Args:
        grid (list of list of int): A 2D grid of integers where
        1 represents land and 0 represents water.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # Found land
                # Check the four neighbors (up, down, left, right)
                if i == 0 or grid[i - 1][j] == 0:  # Up
                    perimeter += 1
                if i == rows - 1 or grid[i + 1][j] == 0:  # Down
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:  # Left
                    perimeter += 1
                if j == cols - 1 or grid[i][j + 1] == 0:  # Right
                    perimeter += 1

    return perimeter
