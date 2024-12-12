#!/usr/bin/python3

def isWinner(x, nums):
    def is_prime(n):
        """Helper function to check if a number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def game(n):
        """Simulates a single round of the game."""
        if n < 2:
            return 'Ben'  # Ben wins if there are no primes for Maria to pick

        # Step 1: Generate a list of available numbers
        available = [True] * (n + 1)
        primes = [i for i in range(2, n + 1) if is_prime(i)]
        
        # Step 2: Simulate the game turn by turn
        turn = 0  # 0 for Maria, 1 for Ben

        while primes:
            # Player picks the smallest prime available
            prime = primes.pop(0)

            # Mark all multiples of the prime as removed
            for i in range(prime, n + 1, prime):
                if available[i]:
                    available[i] = False

            # Switch turns
            turn = 1 - turn

        # Determine the winner
        return 'Maria' if turn == 1 else 'Ben'

    # Step 3: Track the number of wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = game(n)
        if winner == 'Maria':
            maria_wins += 1
        elif winner == 'Ben':
            ben_wins += 1

    # Step 4: Determine the player with the most wins
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    return None
