
"""
Program: Double Each Element in a List
--------------------------------------
This program doubles each element in a given list of numbers.
"""

def double_numbers(numbers: list[int]) -> list[int]:
    """
    Takes a list of numbers and returns a new list with each element doubled.
    """
    return [num * 2 for num in numbers]  # Using list comprehension for efficiency

def main():
    numbers = [1, 2, 3, 4]  # Original list
    doubled_numbers = double_numbers(numbers)  # Get the doubled list
    print(f"Original list: {numbers}")
    print(f"Doubled list: {doubled_numbers}")  # Print the doubled list

if __name__ == '__main__':
    main()
