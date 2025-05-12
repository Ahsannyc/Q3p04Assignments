
import random

def guess_the_number():
    print("🎯 Welcome to the 'Guess the Number' Game! 🤩🎮")
    print("🤖 The computer has chosen a secret number between **1 and 20**. Can you guess it? 🔢🤔")

    # Generate a random number between 1 and 20
    secret_number = random.randint(1, 20)

    attempts = 0  # Track number of guesses

    while True:
        try:
            # Take user input
            user_guess = int(input("💡 Enter your guess (1-20): "))

            # Count the attempts
            attempts += 1

            # Check if the guess is correct
            if user_guess < secret_number:
                print("📉 Too low! Try a **higher** number. ⬆️")
            elif user_guess > secret_number:
                print("📈 Too high! Try a **lower** number. ⬇️")
            else:
                print(f"🎉 **Congratulations!** Wohoooo! 🎊 You guessed the right number in **{attempts}** attempts! 🏆🥳")
                break  # Exit the loop if the guess is correct
        except ValueError:
            print("⚠️ **Oops!** Please enter a valid **number** between 1 and 20. 🔢")

# Call the function to start the game
guess_the_number()
