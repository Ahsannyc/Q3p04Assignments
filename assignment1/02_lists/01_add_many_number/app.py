"""
Program: Sum of a List of Numbers
---------------------------------
This program defines a function that takes a list of numbers 
and returns the sum of those numbers.
"""

def add_many_numbers(numbers: list[int]) -> int:
    """
    Takes in a list of numbers and returns the sum of those numbers.
    """
    return sum(numbers)  # More Pythonic way to sum a list

def main():
    numbers = [1, 2, 3, 4, 5]  # Sample list of numbers
    sum_of_numbers = add_many_numbers(numbers)  # Compute sum
    print(f"The sum of {numbers} is {sum_of_numbers}")  # Improved output formatting

if __name__ == '__main__':
    main()