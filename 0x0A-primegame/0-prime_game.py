#!/usr/bin/python3

def isWinner(x, nums):
    """Determines the player who wins the most rounds in the Prime Game."""
    
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
        
        # Step 1: Generate list of primes up to n
        primes = [i for i in range(2, n + 1) if is_prime(i)]
        available = [True] * (n + 1)
        
        # Step 2: Simulate turns (Maria starts)
        turn = 0  # 0 for Maria, 1 for Ben
        
        while primes:
            prime = primes.pop(0)
            # Mark all multiples of prime as removed
            for i in range(prime, n + 1, prime):
                if available[i]:
                    available[i] = False
            turn = 1 - turn  # Switch turns
        
        # Step 3: Determine the winner
        return 'Maria' if turn == 1 else 'Ben'
    
    # Step 4: Track wins for each player
    maria_wins = ben_wins = 0
    
    for n in nums:
        winner = game(n)
        if winner == 'Maria':
            maria_wins += 1
        elif winner == 'Ben':
            ben_wins += 1
    
    # Step 5: Return the player with most wins
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    
    return None
