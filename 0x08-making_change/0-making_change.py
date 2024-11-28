#!/usr/bin/python3

""" Contains makeChange function"""

def makeChange(coins, total):
    """
    Returns: the fewest number of coins needed to meet total.
    If total is 0 or less, return 0.
    If total cannot be met by any number of coins you have, return -1.
    """
    if not coins:
        return -1
    if total <= 0:
        return 0

    # Sort the coins in descending order for optimal coin usage
    coins.sort(reverse=True)
    change_count = 0

    for coin in coins:
        # Use as many of this coin as possible
        if coin <= total:
            num_coins = total // coin  # Maximum number of coins we can use of this denomination
            total -= num_coins * coin  # Subtract the value from total
            change_count += num_coins  # Add the number of coins used to the total

        # If we've met the total, break out of the loop
        if total == 0:
            return change_count

    return -1  # If total cannot be met with the given coins
