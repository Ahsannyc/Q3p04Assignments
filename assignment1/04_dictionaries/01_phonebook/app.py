
def read_phone_numbers():
    """
    Collects names and phone numbers from user input and stores them in a dictionary.
    Input ends when the user enters a blank name.
    """
    phonebook = {}  # Create an empty dictionary

    while True:
        name = input("Name: ").strip()
        if name == "":  # Stop if user enters a blank name
            break
        number = input("Number: ").strip()
        phonebook[name] = number  # Store name-number pair in dictionary

    return phonebook


def print_phonebook(phonebook):
    """
    Displays all stored names and numbers.
    """
    if not phonebook:
        print("Phonebook is empty.")
    else:
        print("\nPhonebook Entries:")
        for name, number in phonebook.items():
            print(f"{name} -> {number}")


def lookup_numbers(phonebook):
    """
    Allows the user to look up phone numbers by name.
    """
    while True:
        name = input("Enter name to lookup: ").strip()
        if name == "":  # Exit lookup on blank input
            break
        print(phonebook.get(name, f"{name} is not in the phonebook"))


def main():
    """
    Orchestrates the phonebook creation, display, and lookup functionality.
    """
    phonebook = read_phone_numbers()  # Get input
    print_phonebook(phonebook)  # Print stored numbers
    lookup_numbers(phonebook)  # Allow user to search for numbers


# Run the main function when the script is executed
if __name__ == '__main__':
    main()
