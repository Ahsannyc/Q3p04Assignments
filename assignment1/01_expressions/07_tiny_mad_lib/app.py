
"""
Program: Mad Libs Fun!
----------------------
This program prompts the user for an adjective, noun, and verb,
then generates a fun sentence using those words.
"""

# Constant for the beginning of the sentence
SENTENCE_START: str = "GIAIC is fun. I learned to program and used Python to make my"

def main():
    """
    Prompts the user for an adjective, noun, and verb, then prints a fun sentence.
    """
    # Getting user inputs
    adjective: str = input("Please type an adjective and press enter: ")
    noun: str = input("Please type a noun and press enter: ")
    verb: str = input("Please type a verb and press enter: ")

    # Constructing and printing the sentence
    print(f"{SENTENCE_START} {adjective} {noun} {verb}!")

# Ensures the main() function runs when the script is executed
if __name__ == '__main__':
    main()
