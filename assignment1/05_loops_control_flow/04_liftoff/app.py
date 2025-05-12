
def main():
    """
    This program counts down from 10 to 1 and then prints 'Liftoff!'.
    """
    for i in range(10, 0, -1):  # Countdown from 10 to 1
        print(i, end=" ")  # Print numbers on the same line
    
    print("Liftoff!")  # Print Liftoff at the end

# Ensures the main function runs when this script is executed
if __name__ == '__main__':
    main()
