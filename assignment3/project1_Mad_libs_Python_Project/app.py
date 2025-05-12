
import random

print("🎭 Welcome to the Ultimate Mad Libs Story! 🎭\n")
print("😆 Fill in the blanks to create a wild and funny adventure!\n")

name = input("😜 Enter your name: ")
superpower = input("⚡ Enter a superpower: ")
animal = input("🐾 Enter a random animal: ")
place = input("📍 Enter a weird place: ")
food = input("🍕 Enter a delicious food: ")
object = input("🎾 Enter a random object: ")
emotion = input("😊 Enter an emotion: ")
sound = input("🔊 Enter a funny sound (like 'Boing' or 'Kaboom'): ")

actions = [
    "started dancing like a chicken 🐔💃",
    "flew up in the sky ☁️🚀",
    "turned into a frog 🐸😂",
    "sang a song about potatoes 🎶🥔",
    "did 100 push-ups in 2 seconds 💪😆"
]

random_action = random.choice(actions)

story = f"""
📖🌟 **YOUR CRAZY ADVENTURE BEGINS** 🌟📖

One day, {name} woke up with an **amazing** power: {superpower}! ⚡✨
Excited to test it, {name} ran straight to {place}, the strangest place on Earth! 🌍🚀

🐾 Suddenly, a **mysterious** {animal} appeared, blocking the path! 😱
{name} didn't hesitate and used {superpower} 💥 but accidentally {random_action}! 🤯
The {animal} was so {emotion} that it made a loud **'{sound}!'** and vanished into thin air! 🔮💨

🍕 After this wild event, {name} sat down, picked up a {object}, and started munching on {food}.
Little did {name} know, the {object} was actually **magical**! ✨ It whispered,
"Congratulations, {name}! You have just saved {place} from disaster!" 🏆🎉

And that’s how {name} became the **Hero of {place}**! 🦸‍♂️🔥
"""


print("\n" + "="*50)
print(story)
print("="*50 + "\n")
