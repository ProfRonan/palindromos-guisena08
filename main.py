"""Main functions"""


def is_palindrome(string: str) -> bool: 
    string = ''.join(c.lower() for c in string if c.isalnum())
    return string == string[::-1]