# Function to add three copies of a given data to the provided list
def add_three_copies(my_list, data):
    """
    This function modifies the given list by adding three copies of 'data' to it.
    Since lists are mutable, changes persist outside the function.
    """
    for _ in range(3):  # Loop three times
        my_list.append(data)  # Append 'data' to the list


# Main function that handles user input and displays results
def main():
    """
    This function:
    1. Takes user input for a message.
    2. Initializes an empty list.
    3. Displays the list before modification.
    4. Calls add_three_copies to add three copies of the message.
    5. Displays the list after modification.
    """
    message = input("Enter a message to copy: ")  # Prompt user for input
    my_list = []  # Initialize an empty list
    
    print("\nList before modification:", my_list)  # Show initial list state
    
    add_three_copies(my_list, message)  # Modify the list by adding three copies
    
    print("List after modification:", my_list)  # Show the modified list


# Ensures the script runs only when executed directly, not when imported
if __name__ == "__main__":
    main()

