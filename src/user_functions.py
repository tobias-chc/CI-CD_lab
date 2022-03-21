import string


# More elaborated version (copy to src/user_functions.py)
def get_email_from_input():
    """ Contains '@' and '.' """
    email = input("Tell me your email: ")

    if ("@" not in email or "." not in email):
        print('Email is not valid.')
    else:
        return email


def get_user_name_from_input():
    """ Not empty string. No spaces. """
    username = input("Create your user name: ")
    username_set = set(username)

    whitespaces_set = set(string.whitespace)
    whitespaces_condition = len(username_set.intersection(whitespaces_set)) > 0

    if whitespaces_condition:
        print('Username is not valid.')
    else:
        return username


def get_password_from_input():
    """ Password needs to be at least 8 characters long with
    at least one number, one special character and one letter. """
    password = input("Create your password: ")

    # Special character condition
    password_set = set(password)
    special_characters_set = set(string.punctuation)
    special_char_condition = len(password_set.intersection(special_characters_set)) >= 1

    # Digits condition
    digits_set = set(string.digits)
    digits_condition = len(password_set.intersection(digits_set)) >= 1

    # Letter condition
    lower_case_set = set(string.ascii_lowercase)
    upper_case_set = set(string.ascii_uppercase)

    lower_case_condition = len(password_set.intersection(lower_case_set)) >= 1
    upper_case_condition = len(password_set.intersection(upper_case_set)) >= 1

    letter_condition = lower_case_condition and upper_case_condition

    if (len(password) > 8 and special_char_condition and digits_condition and letter_condition):
        return password
    else:
        print('Password is not valid.')
