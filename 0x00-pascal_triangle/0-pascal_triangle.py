#!/usr/bin/python3
"""
0. Generating Pascal's Triangle
"""

def pascal_triangle(n):
    """Defines a function that returns a list of lists
    containing integers that represent Pascal's triangle for the given n.
    """
    res = []
    if n > 0:
        for i in range(1, n + 1):
            level = []
            C = 1
            for j in range(1, i + 1):
                level.append(C)
                C = C * (i - j) // j
            res.append(level)
    return res
