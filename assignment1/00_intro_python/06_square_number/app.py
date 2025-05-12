
def main():
    """
    This program calculates the square of a number.
    It prompts the user for a number, squares it, and displays the result.
    """

    # Prompt the user to enter a number and convert it to a float
    num: float = float(input("Type a number to see its square: "))  

    # Calculate the square of the number
    square: float = num ** 2  

    # Print the result using f-string formatting for better readability
    print(f"{num} squared is {square}")

# Ensures that the main() function runs when the script is executed
if __name__ == '__main__':
    main()
