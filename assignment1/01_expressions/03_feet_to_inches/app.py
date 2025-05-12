
"""
Program: feet_to_inches_converter
---------------------------------
This program converts a measurement in feet to inches.
There are 12 inches in 1 foot.
"""

# Define conversion constant
INCHES_IN_FOOT: int = 12  # 1 foot = 12 inches

def main():
    """
    Prompts the user for a measurement in feet, converts it to inches,
    and displays the result.
    """
    # Get user input for feet and convert it to float
    feet: float = float(input("Enter number of feet: "))

    # Convert feet to inches
    inches: float = feet * INCHES_IN_FOOT

    # Display the result
    print(f"{feet} feet is equal to {inches} inches!")

# Ensures the main() function runs when the script is executed
if __name__ == '__main__':
    main()
