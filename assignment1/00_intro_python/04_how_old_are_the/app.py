
def main():
    """
    This program calculates and displays the ages of Anton, Beth, Chen, Drew, and Ethan
    based on the given age relationships.
    """

    # Given age of Anton
    anton: int = 21  

    # Beth is 6 years older than Anton
    beth: int = anton + 6  

    # Chen is 20 years older than Beth
    chen: int = beth + 20  

    # Drew's age is the sum of Chen's and Anton's ages
    drew: int = chen + anton  

    # Ethan is the same age as Chen
    ethan: int = chen  

    # Printing the ages of all friends
    print("Anton is " + str(anton))
    print("Beth is " + str(beth))
    print("Chen is " + str(chen))
    print("Drew is " + str(drew))
    print("Ethan is " + str(ethan))

# Ensures that the main() function runs when the script is executed
if __name__ == '__main__':
    main()
