
import random  # Import the random module to generate random numbers

# Constants
NUM_ROUNDS: int = 5  # Total rounds in the game
MIN_VALUE: int = 1  # Minimum value for random numbers
MAX_VALUE: int = 100  # Maximum value for random numbers

def main():
    """
    This program implements the High-Low game, where the user tries to guess
    whether their randomly generated number is higher or lower than the computer's number.
    The user earns points for correct guesses.
    """
    
    score = 0  # Initialize user score
    
    print("Welcome to the High-Low Game!")
    print("-" * 32)  # Decorative separator

    # Loop through the game for the given number of rounds
    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")

        # Generate random numbers
        user_number = random.randint(MIN_VALUE, MAX_VALUE)
        computer_number = random.randint(MIN_VALUE, MAX_VALUE)

        # Show the user's number
        print(f"Your number is {user_number}")

        # Get the user's guess with input validation
        while True:
            user_guess = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").strip().lower()
            if user_guess in ["higher", "lower"]:
                break  # Valid input, proceed
            print("Invalid input! Please enter either 'higher' or 'lower'.")

        # Determine if the user's guess is correct
        if (user_guess == "higher" and user_number > computer_number) or (user_guess == "lower" and user_number < computer_number):
            print("You were right!", end=" ")
            score += 1  # Increase score
        else:
            print("Aww, that's incorrect.", end=" ")

        # Reveal the computer's number
        print(f"The computer's number was {computer_number}")
        print(f"Your score is now {score}\n")  # Show updated score

    # Final message based on performance
    print("Thanks for playing!")

    if score == NUM_ROUNDS:
        print("Wow! You played perfectly! 🎉")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well! 👍")
    else:
        print("Better luck next time! 😃")

# Ensures the main function runs when this script is executed
if __name__ == '__main__':
    main()
