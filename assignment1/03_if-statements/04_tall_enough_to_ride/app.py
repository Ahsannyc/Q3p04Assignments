# Define the minimum height required to ride
MINIMUM_HEIGHT: int = 50  # Arbitrary units

def main():
    """
    This function asks the user for their height and checks if they 
    meet the minimum height requirement for the ride.
    """

    # Get the user's height as a floating-point number
    height = float(input("How tall are you? "))

    # Check if the user's height meets the minimum requirement
    if height >= MINIMUM_HEIGHT:
        print("You're tall enough to ride!")  # User meets the height requirement
    else:
        print("You're not tall enough to ride, but maybe next year!")  # Too short for the ride

# Ensures the main function runs only when this script is executed directly
if __name__ == '__main__':
    main()