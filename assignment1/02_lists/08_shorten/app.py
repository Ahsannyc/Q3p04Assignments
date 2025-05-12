
# Define the maximum allowed length for the list
MAX_LENGTH: int = 3

def shorten(lst):
    """
    Removes elements from the end of the list until its length is MAX_LENGTH.
    Prints each removed element.
    If the list is already within the limit, it remains unchanged.
    """
    while len(lst) > MAX_LENGTH:  # Continue removing if list is too long
        last_elem = lst.pop()  # Remove and store the last element
        print(f"Removed: {last_elem}")  # Print the removed element

def get_lst():
    """
    Prompts the user to enter elements for the list one at a time.
    Stops when the user presses Enter without typing anything.
    Returns the final list.
    """
    lst = []  # Initialize an empty list
    while True:
        elem = input("Enter an element (Press Enter to stop): ")  # Prompt user input
        if elem == "":  # Stop if input is empty
            break
        lst.append(elem)  # Add element to list
    return lst  # Return the final list

def main():
    """
    Main function to get user input and call shorten() on the list.
    """
    lst = get_lst()  # Get the list from user input
    print("\nOriginal list:", lst)  # Display original list
    shorten(lst)  # Call shorten() function
    print("Final list:", lst)  # Display list after shortening

# Ensures script runs only when executed directly
if __name__ == '__main__':
    main()
