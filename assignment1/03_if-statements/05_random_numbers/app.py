
# Import the random module to generate random numbers
import random

# Constants defining the number of random numbers and their range
N_NUMBERS: int = 10   # Number of random numbers to generate
MIN_VALUE: int = 1    # Minimum value in the range
MAX_VALUE: int = 100  # Maximum value in the range

def main():
    """
    This function generates and prints 10 random numbers in the range 1 to 100.
    Each time the program runs, it should output different numbers.
    """

    # Generate a list of 10 random numbers using randint
    random_numbers = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(N_NUMBERS)]

    # Print the generated numbers separated by spaces
    print(" ".join(map(str, random_numbers)))

# Ensures the main function runs only when this script is executed directly
if __name__ == '__main__':
    main()
