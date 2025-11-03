def roll_two_d6() -> tuple[int, int]:
    import random
    play1 = random.randint(1, 6)
    play2 = random.randint(1, 6)
    return play1, play2

def is_bust(score: int) -> bool:
    if score > 100:
        return True
    else:
        return False
    
def is_exact_100(score: int) -> bool:
    if score == 100:
        return True
    else:
        return False
    
def closer_to_target(a: int, b: int, target: int = 100) -> int | None:
    if a > b and a < target:
        return 1
    elif b > a and b < target:
        return 2
    else:
        None

def tie_breaker():
    player1 = []
    player2 = []
    for i in range(0, 2):

    tie = roll_two_d6()
    while tie[0] == tie[1]:
        tie = roll_two_d6()
    if tie[0] > tie[1]:
        return 1
    else:
        return 2
    
def turn_decision(input_fn) -> str:
    turn_type = input("enter either 'r' to roll the dice or 'p' to pass your turn: ")
    while turn_type != "r" and turn_type != "p":
        turn_type = input("you seem to have entered an invalid input. please enter either 'r' to roll the dice or 'p' to pass your turn: ")
    return input_fn()

# def play_game():
#     pla