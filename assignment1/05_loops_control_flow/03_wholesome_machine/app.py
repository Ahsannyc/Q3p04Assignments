
# Constant storing the correct affirmation
AFFIRMATION: str = "I am capable of doing anything I put my mind to."

def main():
    """
    This program repeatedly prompts the user to type a positive affirmation 
    until they enter it correctly.
    """

    # Prompt the user to type the affirmation
    print("Please type the following affirmation: " + AFFIRMATION)

    user_feedback = input()  # Get user's input
    
    # Keep asking until the user enters the correct affirmation
    while user_feedback != AFFIRMATION:  
        print("That was not the affirmation.")  # Let them know they made a mistake

        # Ask again
        print("Please type the following affirmation: " + AFFIRMATION)
        user_feedback = input()

    # User entered the correct affirmation
    print("That's right! :)")

# Ensures the main function runs when this script is executed
if __name__ == '__main__':
    main()
