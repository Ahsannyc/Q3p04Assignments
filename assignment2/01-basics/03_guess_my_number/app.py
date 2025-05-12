
import random  # Importing the random module to generate a random number

def main():
    """
    This program generates a random number between 1 and 99.
    The user must guess the number, receiving hints if their guess is too high or too low.
    The game continues until the user correctly guesses the number.
    """

    # Generate a secret random number between 1 and 99
    secret_number: int = random.randint(1, 99)
    
    print("I am thinking of a number between 1 and 99...")  # Inform the user about the game
    
    # Ask the user for their first guess
    guess = int(input("Enter a guess: "))
    
    # Loop continues until the user guesses the correct number
    while guess != secret_number:
        if guess < secret_number:  # Check if guess is too low
            print("Your guess is too low")
        else:  # If guess is not too low, then it must be too high
            print("Your guess is too high")
            
        print()  # Print an empty line to keep the console output tidy
        
        # Get a new guess from the user
        guess = int(input("Enter a new guess: "))  
    
    # When the loop ends, it means the correct number was guessed
    print(f"Congrats! The number was: {secret_number}")  # Display the winning message

# Ensures the main function runs when this script is executed
if __name__ == '__main__':
    main()
