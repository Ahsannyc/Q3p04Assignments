
import random

def computer_guess():
    print("🎯 Welcome to the 'Guess the Number' Game! 🤖🎲")
    print("🤔 Think of a number between **1 and 20**, and I'll try to guess it! 🔢")

    low = 1
    high = 20
    attempts = 0

    while True:
        if low > high:
            print("⚠️ Something went wrong! Did you change your number? 😲")
            break

        guess = random.randint(low, high)
        attempts += 1

        print(f"🤖 My guess is: **{guess}** 🎯")
        feedback = input("📢 Is it (H)igh, (L)ow, or (C)orrect? ").lower()

        if feedback == "c":
            print(f"🎉 Wohoooo! 🥳 I guessed it in **{attempts}** attempts! 🏆🔥")
            break
        elif feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
        else:
            print("⚠️ Please enter **H, L, or C** only! 📝")

computer_guess()
