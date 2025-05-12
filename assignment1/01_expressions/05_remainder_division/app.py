"""
Program: division_calculator
----------------------------
This program asks the user for two numbers and calculates:
- The quotient (integer division)
- The remainder of the division
"""

def main():
    """
    Prompts the user to input two integers, then calculates and displays 
    the quotient and remainder.
    """
    # Get user input and convert to integers
    dividend: int = int(input("Please enter an integer to be divided: "))
    divisor: int = int(input("Please enter an integer to divide by: "))

    # Check if the divisor is zero to avoid division errors
    if divisor == 0:
        print("Error: Division by zero is not allowed.")
        return

    # Calculate quotient and remainder
    quotient: int = dividend // divisor  # Integer division
    remainder: int = dividend % divisor  # Modulo operation

    # Display the result using f-strings for better readability
    print(f"The result of this division is {quotient} with a remainder of {remainder}")

# Ensures the main() function runs when the script is executed
if __name__ == '__main__':
    main()