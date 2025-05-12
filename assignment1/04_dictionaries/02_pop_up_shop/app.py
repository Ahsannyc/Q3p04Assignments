def main():
    """
    This program calculates the total cost of fruits a user wants to buy.
    - It uses a dictionary to store fruit names and their respective prices.
    - It asks the user how many of each fruit they want.
    - It validates user input to ensure correct values are entered.
    - Finally, it displays the total cost of the selected fruits.
    """

    # Dictionary containing fruit names as keys and their prices as values
    fruits = {
        'apple': 1.5,
        'durian': 50,
        'jackfruit': 80,
        'kiwi': 1,
        'rambutan': 1.5,
        'mango': 5
    }

    total_cost = 0  # Variable to track total cost

    # Loop through each fruit in the dictionary
    for fruit, price in fruits.items():
        while True:
            try:
                # Ask the user how many of this fruit they want to buy
                amount_bought = int(input(f"How many ({fruit}) do you want?: ").strip())

                # Ensure the user doesn't enter a negative number
                if amount_bought < 0:
                    print("Please enter a valid non-negative number.")
                    continue  # Ask again if the input is invalid

                break  # Exit loop if input is valid

            except ValueError:
                # Handle cases where the input is not a valid integer
                print("Invalid input. Please enter a valid number.")

        # Calculate the cost for this fruit and add it to the total cost
        total_cost += price * amount_bought

    # Print the final total cost formatted to 2 decimal places
    print(f"\nYour total is ${total_cost:.2f}")

# Standard Python boilerplate to ensure main() runs when the script is executed
if __name__ == '__main__':
    main()