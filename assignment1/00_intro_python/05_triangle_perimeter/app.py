
def main():
    """
    This program calculates the perimeter of a triangle.
    It prompts the user to enter the lengths of all three sides,
    sums them up, and prints the total perimeter.
    """

    # Prompt the user to enter the length of each side of the triangle
    side1: float = float(input("What is the length of side 1? "))  
    side2: float = float(input("What is the length of side 2? "))  
    side3: float = float(input("What is the length of side 3? "))  

    # Calculate the perimeter (sum of all sides)
    perimeter: float = side1 + side2 + side3  

    # Print the calculated perimeter with proper formatting
    print(f"The perimeter of the triangle is {perimeter}")

# Ensures that the main() function runs when the script is executed
if __name__ == '__main__':
    main()
