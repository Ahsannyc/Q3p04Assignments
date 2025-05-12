def main():
    """
    This function prints the first 20 even numbers.
    The first even number is 0.
    """
    
    # Loop runs 20 times (i goes from 0 to 19)
    for i in range(20):  
        # Multiply i by 2 to get even numbers (0, 2, 4, ..., 38)
        print(i * 2, end=" ")  # Print numbers in a single line with spaces

# Ensures the main function runs only when this script is executed directly
if __name__ == "__main__":
    main()