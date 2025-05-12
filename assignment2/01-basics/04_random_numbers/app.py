
import random  # Import the random module to generate random numbers

# Constants
N_NUMBERS: int = 10  # Number of random numbers to generate
MIN_VALUE: int = 1  # Minimum value in the range
MAX_VALUE: int = 100  # Maximum value in the range

def main():
    """
    This program prints 10 random numbers in the range of 1 to 100.
    Each time the program runs, different random numbers will be generated.
    """

    # Generate and print 10 random numbers using a loop
    for _ in range(N_NUMBERS):  
        print(random.randint(MIN_VALUE, MAX_VALUE), end=" ")  # Print numbers on the same line
    
    print()  # Print a newline after all numbers are displayed

# Ensures the main function runs when this script is executed
if __name__ == '__main__':
    main()
