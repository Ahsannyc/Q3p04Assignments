
from hashlib import sha256  # Importing the SHA256 hashing function

def login(email, stored_logins, password_to_check):
    """
    Checks if the given password matches the stored password for a specific email.

    - The function hashes the `password_to_check` using SHA256.
    - It then compares the hashed value with the one stored in `stored_logins`.
    - If they match, login is successful (returns True), otherwise, it fails (returns False).

    Parameters:
        email (str): The email of the user trying to log in.
        stored_logins (dict): A dictionary mapping emails to their hashed passwords.
        password_to_check (str): The password entered by the user.

    Returns:
        bool: True if login is successful, False otherwise.
    """

    # Check if the email exists in the dictionary before comparing
    if email in stored_logins and stored_logins[email] == hash_password(password_to_check):
        return True  # Login successful
    
    return False  # Login failed


def hash_password(password):
    """
    Hashes the given password using the SHA256 algorithm.
    
    - The password is first converted to bytes using `.encode()`
    - Then, it's passed through SHA256 hashing to generate a unique hash.

    Parameters:
        password (str): The password to be hashed.

    Returns:
        str: The hashed representation of the password.
    """
    return sha256(password.encode()).hexdigest()


def main():
    """
    This function simulates a basic password authentication system.
    
    - A dictionary `stored_logins` stores user emails and their hashed passwords.
    - The program then tests various login attempts by calling `login()`.
    - The results (True or False) are printed to indicate if login was successful.
    """

    # Pre-stored user credentials (emails mapped to hashed passwords)
    stored_logins = {
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",  # password: "password"
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",  # password: "Karel"
        "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"  # password: "123!456?789"
    }

    # Testing the login function with different cases
    print(login("example@gmail.com", stored_logins, "word"))  # False (Incorrect password)
    print(login("example@gmail.com", stored_logins, "password"))  # True (Correct password)

    print(login("code_in_placer@cip.org", stored_logins, "Karel"))  # True (Correct password)
    print(login("code_in_placer@cip.org", stored_logins, "karel"))  # False (Incorrect case-sensitive password)

    print(login("student@stanford.edu", stored_logins, "password"))  # False (Wrong password)
    print(login("student@stanford.edu", stored_logins, "123!456?789"))  # True (Correct password)


# Ensures `main()` runs only when this script is executed directly
if __name__ == '__main__':
    main()
