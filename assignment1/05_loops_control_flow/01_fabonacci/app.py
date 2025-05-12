# Define a constant for the maximum Fibonacci term value
MAX_TERM_VALUE: int = 10000  

def main():
    """
    This program prints the Fibonacci sequence, starting from 0,
    and continues generating terms until the value reaches 10,000.
    """

    curr_term = 0  # The first Fibonacci number (Fib(0))
    next_term = 1  # The second Fibonacci number (Fib(1))
    
    # Continue generating Fibonacci terms as long as the current term is within the limit
    while curr_term <= MAX_TERM_VALUE:
        print(curr_term)  # Print the current Fibonacci number
        
        # Compute the next term in the sequence
        term_after_next = curr_term + next_term

        # Update values for the next iteration
        curr_term = next_term
        next_term = term_after_next

# Ensures `main()` runs only when this script is executed directly
if __name__ == '__main__':
    main()