def main():
    # Prompt user for temperature in Farenheit (can include decimals)
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))   # Get input and convert to float

    # Convert Fahrenheit to Celsius using the formula: (F - 32) * 5.0/9.0
    Celsius = (fahrenheit - 32)  * 5.0 / 9.0  # Using float division with 5.0 and 9.0

    # Output the result in the specified format: Temperature: [Fahrenheit]F = [Celsius]C
    print("Temperature: " + str(fahrenheit) + "F = " + str(Celsius) + "C")

 # This provided line is required at the end of 
 # python file to call the main() function.
if __name__ == '__main__':
    main()   
    

