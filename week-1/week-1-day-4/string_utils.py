def reverse_string(string: str):
    return string[::-1]

def is_palindrome(string: str):
    if string == string[::-1]:
        return "is a palindrome"
    else:
        return "not a palindrome"