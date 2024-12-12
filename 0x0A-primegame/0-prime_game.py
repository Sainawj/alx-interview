#!/usr/bin/python3
"""0. Prime Game - Maria and Ben are playing a game"""


def isWinner(x, nums):
    """Determines the winner of the Prime Game for multiple rounds.

    Args:
        x (int): The number of rounds.
        nums (list): A list of numbers, where each number represents the
        upper limit of a round.
   
    Returns:
        str: The name of the player who wins the most
        rounds ('Maria' or 'Ben'),
             or None if there is no clear winner.
    """
    # Check for invalid input (negative rounds or None for nums)
    if x <= 0 or nums is None:
        return None
    # Ensure that the number of rounds matches the length of the nums list
    if x != len(nums):
        return None

    # Initialize counters for Ben and Maria's wins
    ben = 0
    maria = 0

    # Create a list 'a' to mark prime numbers
    (1 for possible primes, 0 for non-primes)
    a = [1 for x in range(sorted(nums)[-1] + 1)]
    # Mark 0 and 1 as non-prime numbers
    a[0], a[1] = 0, 0

    # Iterate through the list and remove multiples of primes
    for i in range(2, len(a)):
        rm_multiples(a, i)

    # Loop through each round and determine the winner
    for i in nums:
        # If the sum of prime numbers up to 'i' is even, Ben wins the round
        if sum(a[0:i + 1]) % 2 == 0:
            ben += 1
        else:  # Otherwise, Maria wins
            maria += 1

    # Return the player with the most wins
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def rm_multiples(ls, x):
    """Removes multiples of prime numbers from the list.

    Args:
        ls (list): The list of prime numbers.
        x (int): The prime number whose multiples should be marked as non-prime.
    """
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0  # Mark the multiple as non-prime
        except (ValueError, IndexError):
            break
