
def main():
    """
    This program prints the first 20 even numbers using a loop.
    Instead of writing 20 print statements, it efficiently generates even numbers using multiplication.
    """

    # Loop runs 20 times (i from 0 to 19)
    for i in range(20):  
        print(i * 2)  # Each iteration prints an even number (0, 2, 4, ... 38)
   
# Ensures `main()` runs only when this script is executed directly
if __name__ == "__main__":
    main()
