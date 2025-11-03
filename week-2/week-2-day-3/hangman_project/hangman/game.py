

def convert_to_(word: str) -> list[str]:
    secret = []
    for index in range(len(word)):
        secret.append("_")
    return secret

user_input = print(input("enter a single letter: "))

def validity_check(letter: str) -> bool:
    if user_input != str or len(user_input) > 1:
        return False
    else: return True

if validity_check:
    