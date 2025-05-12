
def main():
    """
    This function asks the user for a year and checks if it's a leap year
    based on the rules of the Gregorian calendar.
    """

    # Get the year input from the user and convert it to an integer
    year = int(input('Please input a year: '))

    # Check if the year is a leap year using the given conditions
    if year % 4 == 0:  # A year must be divisible by 4 to be a leap year
        if year % 100 == 0:  # If divisible by 100, an extra condition applies
            if year % 400 == 0:  # If divisible by 400, it is a leap year
                print("That's a leap year!")
            else:  # Divisible by 100 but not by 400, so not a leap year
                print("That's not a leap year.")
        else:  # Divisible by 4 but not by 100, so it's a leap year
            print("That's a leap year!")
    else:  # Not divisible by 4, so it's not a leap year
        print("That's not a leap year.")

# Ensures the main function runs only when this script is executed directly
if __name__ == '__main__':
    main()
