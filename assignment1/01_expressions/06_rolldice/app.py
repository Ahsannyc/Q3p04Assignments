"""
Program: Dice Roller
--------------------
This program simulates rolling two dice and prints:
- The number of sides on each die
- The result of each roll
- The total sum of both dice
"""

import random  # Import the random module to simulate rolling dice

# Constant for the number of sides on each die
NUM_SIDES: int = 6  

def roll_dice():
    """
    Rolls a single die and returns the result.
    """
    return random.randint(1, NUM_SIDES)

def main():
    """
    Simulates rolling two dice and prints the results.
    """
    # Roll two dice
    die1: int = roll_dice()
    die2: int = roll_dice()

    # Calculate the total
    total: int = die1 + die2

    # Display the results
    print(f"Each die has {NUM_SIDES} sides.")
    print(f"First die roll: {die1}")
    print(f"Second die roll: {die2}")
    print(f"Total of two dice: {total}")

# Ensures the main() function runs when the script is executed
if __name__ == '__main__':
    main()