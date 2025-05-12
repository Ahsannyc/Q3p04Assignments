
def get_first_element(lst):
    """
    Prints the first element of a provided list.
    The list is guaranteed to be non-empty.
    """
    print("First element:", lst[0])  # Print the first element of the list


def get_lst():
    """
    Prompts the user to enter one element at a time to create a list.
    The user can press 'Enter' without typing anything to stop adding elements.
    Returns the final list.
    """
    lst = []  # Initialize an empty list

    while True:
        elem = input("Enter an element (Press Enter to stop): ")  # Ask for input
        if elem == "":  # Stop if the input is empty
            break
        lst.append(elem)  # Append element to the list
    
    return lst  # Return the constructed list


def main():
    """
    - Calls get_lst() to get a user-defined list.
    - Calls get_first_element() to print the first element of the list.
    """
    lst = get_lst()  # Get the list from user input
    get_first_element(lst)  # Print the first element of the list


# Ensures the script runs only when executed directly
if __name__ == '__main__':
    main()
