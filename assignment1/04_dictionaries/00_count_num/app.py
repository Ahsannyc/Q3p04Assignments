
def get_user_numbers():
    """
    Collects numbers from user input and stores them in a list.
    Input ends when the user enters a blank line.
    """
    user_numbers = []
    while True:
        user_input = input("Enter a number: ")

        # Stop taking input if the user enters a blank line
        if user_input == "":
            break
        
        # Convert input to an integer and store it in the list
        user_numbers.append(int(user_input))

    return user_numbers


def count_nums(num_lst):
    """
    Counts occurrences of each number in the list using a dictionary.
    """
    num_dict = {}
    for num in num_lst:
        num_dict[num] = num_dict.get(num, 0) + 1  # Using .get() to simplify the logic

    return num_dict


def print_counts(num_dict):
    """
    Prints the count of each number in the dictionary.
    """
    for num, count in num_dict.items():
        print(f"{num} appears {count} times.")


def main():
    """
    Orchestrates user input, counting occurrences, and displaying results.
    """
    user_numbers = get_user_numbers()  # Get numbers from the user
    num_dict = count_nums(user_numbers)  # Count occurrences
    print_counts(num_dict)  # Print results


# Ensures the main function runs only when the script is executed directly
if __name__ == '__main__':
    main()
