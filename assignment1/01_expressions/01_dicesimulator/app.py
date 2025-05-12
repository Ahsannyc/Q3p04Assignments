"""
Program: dicesimulator
----------------------
This program simulates rolling two dice three times.
It prints the results of each roll and demonstrates how variable scope works.
"""

# Import the random module to generate random numbers
import random

# Define a constant for the number of sides on each die
NUM_SIDES = 6  

def roll_dice():
    """
    Simulates rolling two dice and prints their sum.
    The numbers are generated randomly between 1 and NUM_SIDES.
    """
    die1: int = random.randint(1, NUM_SIDES)  # Roll the first die
    die2: int = random.randint(1, NUM_SIDES)  # Roll the second die
    total: int = die1 + die2  # Calculate the sum of the two dice
    
    # Print the results of the dice roll
    print(f"Die 1: {die1}, Die 2: {die2} -> Total: {total}")

def main():
    """
    Demonstrates variable scope.
    A local variable 'die1' is defined inside main() to show that 
    it is separate from the 'die1' variable inside roll_dice().
    """
    die1: int = 10  # Local variable inside main()
    print(f"die1 in main() starts as: {die1}")  # Show its initial value
    
    # Call the roll_dice() function three times
    roll_dice()
    roll_dice()
    roll_dice()
    
    # Show that 'die1' inside main() remains unchanged
    print(f"die1 in main() is still: {die1}")

# Ensures the main() function runs when the script is executed
if __name__ == '__main__':
    main()