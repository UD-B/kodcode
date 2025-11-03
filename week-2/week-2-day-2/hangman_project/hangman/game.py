from words import choose_secret_word
def init_state(secret: str, max_tries: int) -> dict:
   
    display = []
    for i in range(0, len(secret)):
        display.append("_")
    print(f"your hangman word is '{display}'.")
    return {
        "secret": secret,
        "display": display,
        "guessed": {""},
        "wrong_guesses": 0,
        "max_tries": max_tries
    }
# start_game = init_state("dad",3)

def validate_guess(ch: str, guessed: set[str]) -> tuple[bool, str]:
    validation = ()
    for ch in guessed:
        if ch != str or len(ch) > 1 or ch in guessed:
            validation = (False, "invalid charachter.")
        validation = (True, "valid charachter.")
    return validation

def apply_guess(state: dict, ch: str):
    result = letter_check(ch,state['secret'])
    if result:
        pass
    else: state['gueesed'].add(ch)


def letter_check(ch,word):
    return ch in word


def handle_true():
    


# print(letter_check(2,[1,2,3,4]))



    # if ch in state["secret"]:
    #     for index in 
    #     return True
    # state["gueesed"].add(ch)
    # return False