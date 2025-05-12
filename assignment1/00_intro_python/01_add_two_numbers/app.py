"""
This program asks the user for two integers and prints their sum.
"""

def main():   
    # Introductory message to tell user what the program does
    print("Thid program adds two numbers.")
    # 1. Prompt the user to enter the first number
    # 2. Read the input and convert it to an integer  
    num1 = input("Enter first number: ")   # Get first number as string
    num1 = int(num1)
                       # Convert string to integer
    
    # 3. Prompt the user to enter the second number
    # 4. Read the input and convert it to an integer
    num2 = input("Enter second number: ") # Get second number as string
    num2 = int(num2)    # Convert string to integer
                        
    
    # 5. Calculate the sum of the two numbers
    total = num1 + num2              # Add the two integers
    
    # 6. Print the total sum with an appropriate message
    print("The total is " + str(total) + ".")     # Convert sum to string and display

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ =='__main__':
    main()
