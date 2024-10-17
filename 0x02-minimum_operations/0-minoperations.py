#!/usr/bin/python3
"""
Minimum Operations Module

This module provides a function to calculate the minimum number of
operations required to achieve exactly n characters of 'H' using
only "Copy All" and "Paste" operations.

The function takes an integer n and returns the minimum number of
operations needed, or 0 if n is impossible to achieve.
"""


def minOperations(n):
    """
    Calculate the minimum number of operations to reach exactly n
    characters of 'H'.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The minimum number of operations needed to achieve n
             'H' characters, or 0 if it is impossible.
    """
    if n <= 1:
        return 0  # If n <= 1, it's impossible to achieve

    operations = 0  # Initialize the operation count
    divisor = 2  # Start checking for divisors from 2

    while n > 1:  # While n is greater than 1
        while n % divisor == 0:  # While n is divisible by divisor
            operations += divisor  # Add divisor to operations count
            n //= divisor  # Reduce n by the divisor
        divisor += 1  # Increment divisor to check the next integer

    return operations  # Return total number of operations


# Example test cases
if __name__ == "__main__":
    n = 4
    print("Min # of operations to reach {} char: {}".format(n,
          minOperations(n)))

    n = 12
    print("Min # of operations to reach {} char: {}".format(n,
          minOperations(n)))

    n = 9
    print("Min # of operations to reach {} char: {}".format(n,
          minOperations(n)))
