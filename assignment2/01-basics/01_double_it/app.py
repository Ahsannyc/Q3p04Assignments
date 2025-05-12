
def main():
    # Ask the user to enter a number and convert it to an integer
    curr_value = int(input("Enter a number: "))

    # Loop until the current value is 100 or greater
    while curr_value < 100:
        curr_value *= 2  # Double the value
        print(curr_value, end=" ")  # Print the new value on the same line with space

# Call the main function to start the program
if __name__ == '__main__':
    main()
