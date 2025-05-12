
"""
Program: hypotenuse_calculator
------------------------------
This program calculates the hypotenuse of a right triangle using
the Pythagorean theorem: BC² = AB² + AC².
"""

import math  # Import math module to use sqrt function

def main():
    """
    Prompts the user for the lengths of two perpendicular sides of a right triangle,
    calculates the hypotenuse using the Pythagorean theorem, and displays the result.
    """
    # Get user input and convert to float
    ab: float = float(input("Enter the length of AB: "))
    ac: float = float(input("Enter the length of AC: "))

    # Calculate the hypotenuse
    bc: float = math.sqrt(ab**2 + ac**2)

    # Display the result with a formatted output
    print(f"The length of BC (the hypotenuse) is: {bc:.2f}")

# Ensures the main() function runs when the script is executed
if __name__ == '__main__':
    main()
