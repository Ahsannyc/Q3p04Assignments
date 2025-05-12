
def main():
    """
    This program asks the user to enter a number, doubles it, and prints the results
    until the value is 100 or greater.
    """
    curr_value = int(input("Enter a number: "))  # Get user input
    
    while curr_value < 100:  # Loop until the value reaches or exceeds 100
        curr_value *= 2  # Double the value
        print(curr_value, end=" ")  # Print on the same line

# Ensures the main function runs when this script is executed
if __name__ == '__main__':
    main()
