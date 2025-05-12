
import random

def play_game():
    print("🎮 Welcome to Rock, Paper, Scissors! ✂️🪨📄")

    choices = ["rock", "paper", "scissors"]
    user_choice = input("🤔 Choose: Rock, Paper, or Scissors? ").lower()

    if user_choice not in choices:
        print("⚠️ Invalid choice! Please choose Rock, Paper, or Scissors. ❌")
        return

    computer_choice = random.choice(choices)

    print(f"🧑 You chose: {user_choice.capitalize()} 🎭")
    print(f"🤖 Computer chose: {computer_choice.capitalize()} 💻")

    if user_choice == computer_choice:
        print("😲 It's a tie! Try again. 🔄")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("🎉 You win! 🏆🔥")
    else:
        print("😢 You lose! Better luck next time. 💀")

play_game()
