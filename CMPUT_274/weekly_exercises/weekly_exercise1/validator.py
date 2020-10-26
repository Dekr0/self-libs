# ---------------------------------------------------
#   Name : Chengxuan Li
#   ID: 1631060
#   CMPUT 274, Fall 2020
#
#   Exercise 1: Password Validator
# ---------------------------------------------------


from random import choice, randint, sample, shuffle


# Global variables (constants)

DIGITS = set([chr(i) for i in range(48, 58)]) # 0 ~ 9 (digits)
FORB_CHARS = {" ", "@", "#"} # forbidden characters
LOWER_CHARS = set([chr(i) for i in range(97, 123)]) # a ~ z (lowercase characters)
SPEC_CHARS = set("!-$%&'()*+,./:;<=>?_[]^`{|}~") # special characters


def validate(password):
    """ Analyzes an input password to determine if it is "Secure", "Insecure", or "Invalid" based on the assignment description criteria.

    Arguments:
        password (string): a string of characters

    Returns:
        result (string): either "Secure", "Insecure", or "Invalid". 
    """

    # check password length and forbidden characters
    password = list(password)
    if FORB_CHARS.intersection(password) or len(password) < 8:
        return "Invalid"

    # check whether the password satisfies the criteria of a secure password
    if all([
            any(i.isupper() for i in password),  
            LOWER_CHARS.intersection(password),
            DIGITS.intersection(password),
            SPEC_CHARS.intersection(password),
            ]
            ):
        return "Secure"
    
    return "Insecure"


def generate(n):
    """ Generates a password of length n which is guaranteed to be Secure according to the given criteria.

    Arguments:
        n (integer): the length of the password to generate, n >= 8.

    Returns:
        secure_password (string): a Secure password of length n. 
    
    Notes: 
        Number of upper letters, lower letters, digits and special characters depend on the length of the password, which means that they are propotional (their number will increase as the length of the password increase). 
    """
    
    try:
        length = int(n)
    except (TypeError, ValueError):
        return "Invalid Input"
    
    if length < 8:
        return "The length of a password must greater or equal to 8"
    
    # Generates specific amount of random lowercase letters a~z (ascii table 97~122).
    password = [choice(list(LOWER_CHARS)) for i in range(length-length//4*2)]

    # Randomly samples certain number of lowercase letters and convert them into uppercase.
    for char in sample(password, length//3):
        password[password.index(char)] = char.upper()
    
    # Inserts a certain number of digits and special characters to fill up the remaining spots. Insert locations are randomly selected.
    for i in range(length//4):
        password.insert(randint(0, length), choice(list(DIGITS)))
        password.insert(randint(0, length), choice(list(SPEC_CHARS)))
    shuffle(password)

    return "".join(password)


if __name__ == "__main__":
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 validator.py". This can be useful for
    # testing your implementations.
    
    
    # For the use of self-made testcases with Makefile
    
    """
    password = input()
    print(validate(password))
    length = input().strip()
    test_pwd = generate(length)
    print(test_pwd, validate(test_pwd)) # Again, make sure that the generate password is guaranteed secure.
    """
