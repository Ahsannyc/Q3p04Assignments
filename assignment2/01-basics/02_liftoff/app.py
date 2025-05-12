
def main():
    """
    This program prints a countdown from 10 to 1, followed by "Liftoff!".
    It simulates a spaceship launch sequence.
    """

    # Loop from 10 down to 1
    for i in range(10, 0, -1):  # Start at 10, go down to 1, decreasing by 1 each time
        print(i, end=" ")  # Print numbers on the same line with space

    print("Liftoff!")  # Print "Liftoff!" after the countdown ends

# Ensures the main function runs when this script is executed
if __name__ == '__main__':
    main()
