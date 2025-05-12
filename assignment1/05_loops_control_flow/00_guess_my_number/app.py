import random  # Importing the random module to generate a random number

def main():
    """
    This program generates a random number between 1 and 99.
    The user has to guess the number, receiving hints if the guess is too high or too low.
    The game continues until the correct number is guessed.
    """

    # Generate a random number between 1 and 99
    secret_number = random.randint(1, 99)
    
    print("I am thinking of a number between 1 and 99...")  # Inform the user about the game
    
    # Get the user's first guess
    guess = int(input("Enter a guess: "))

    # Keep asking the user for guesses until they find the correct number
    while guess != secret_number:
        if guess < secret_number:  # If the guess is too low
            print("Your guess is too low")
        else:  # If the guess is too high
            print("Your guess is too high")
        
        print()  # Print an empty line to make the console output cleaner
        
        # Ask the user for a new guess
        guess = int(input("Enter a new guess: "))
    
    # When the user guesses the correct number, print a success message
    print("Congrats! The number was: " + str(secret_number))

# Ensures `main()` runs only when this script is executed directly
if __name__ == '__main__':
    main()