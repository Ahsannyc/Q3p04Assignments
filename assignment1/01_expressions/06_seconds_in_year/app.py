"""
Program: Seconds in a Year
--------------------------
This program calculates the total number of seconds in a year
using constants for days, hours, minutes, and seconds.
"""

# Constants for time calculations
DAYS_PER_YEAR: int = 365
HOURS_PER_DAY: int = 24
MINUTES_PER_HOUR: int = 60
SECONDS_PER_MINUTE: int = 60

def calculate_seconds_in_year():
    """
    Computes the total number of seconds in a year.
    """
    return DAYS_PER_YEAR * HOURS_PER_DAY * MINUTES_PER_HOUR * SECONDS_PER_MINUTE

def main():
    """
    Prints the total number of seconds in a year in a nicely formatted statement.
    """
    total_seconds = calculate_seconds_in_year()
    print(f"There are {total_seconds} seconds in a year!")

# Ensures the main() function runs when the script is executed
if __name__ == '__main__':
    main()