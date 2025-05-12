
def main():
    """
    Continuously asks the user to enter values and stores them in a list.
    Stops when the user presses Enter without typing anything.
    Finally, prints the list.
    """
    lst = []  # Initialize an empty list to store user inputs

    while True:
        val = input("Enter a value (Press Enter to stop): ")  # Prompt user for input
        if val == "":  # Stop if input is empty
            break
        lst.append(val)  # Add the input to the list

    print("Here's the list:", lst)  # Print the final list


# Ensures the script runs only when executed directly
if __name__ == '__main__':
    main()
