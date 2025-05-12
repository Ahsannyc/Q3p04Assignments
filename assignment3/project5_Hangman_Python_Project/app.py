
import random

# Expanded word list
words = [
    "python", "developer", "hangman", "programming", "computer", "science",  # Tech
    "elephant", "kangaroo", "crocodile", "penguin", "dolphin", "cheetah",  # Animals
    "strawberry", "pineapple", "chocolate", "spaghetti", "sandwich", "cucumber",  # Foods
    "Pakistan", "Germany", "Canada", "Australia", "Brazil", "Japan",  # Countries
    "football", "basketball", "cricket", "swimming", "baseball", "badminton"  # Sports
]

# Randomly select a word
word = random.choice(words).lower()  # Ensure lowercase
word_letters = set(word)  # Unique letters in the word
guessed_letters = set()  # Letters guessed by the user
attempts = 6  # Total chances

print("🎭 Welcome to Hangman! Can you guess the word? 🔤")

while attempts > 0 and word_letters:
    # Show current word progress
    display_word = [letter if letter in guessed_letters else "_" for letter in word]
    print(" ".join(display_word))

    # Get user input
    guess = input("🔤 Guess a letter: ").lower()

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter! Try again.")
    elif guess in word_letters:
        guessed_letters.add(guess)
        word_letters.remove(guess)
        print("✅ Correct!")
    else:
        attempts -= 1
        print(f"❌ Wrong! You have {attempts} attempts left.")

        # Hangman Figure (Fix: Adjusted index)
        hangman_stages = [
            "  😵💀  ",   # 6th attempt gone
            "  😨|   ",   # 5th attempt gone
            "  😰/|  ",   # 4th attempt gone
            "  🥶/|\ ",  # 3rd attempt gone
            "  🫣/|\ ",  # 2nd attempt gone
            "  😱/|\ /  " # 1st attempt gone
        ]
        if attempts < 6:
            print(hangman_stages[5 - attempts])  # Fix: Adjusted index

# Game Over Check
if not word_letters:
    print(f"🎉 Congratulations! You guessed the word: {word.upper()} 🏆")
else:
    print(f"💀 Game Over! The correct word was: {word.upper()}")
