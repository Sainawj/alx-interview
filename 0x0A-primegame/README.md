# Prime Game

This Python script implements a game where two players, Maria and Ben, take turns picking prime numbers from a set of consecutive integers from 1 to `n`. Each time a player picks a prime, all its multiples are removed from the set. The player who cannot make a move loses the round.

## Functionality

- **`isWinner(x, nums)`**: Determines the winner of `x` rounds of the game based on the values in `nums`, where each value represents the number `n` for a given round.
- Players alternate turns, with Maria going first. The game continues until all prime numbers are removed.
- The function returns the player who wins the most rounds, or `None` if there's a tie.

## Usage

To use the script:

```python
isWinner(x, nums)

