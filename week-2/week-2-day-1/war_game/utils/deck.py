def create_card(rank: str, suite: str) -> dict:
    upper_rank = rank.upper()
    upper_suite = suite.upper()
    value_of_ranks = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14
        }
    card = {"rank": rank, "suite": suite, "value": value_of_ranks[rank]}
    return card

def compare_card(p1_card: dict, p2_card: dict) -> str:
    if p1_card["value"] > p2_card["value"]:
        return "p1"
    elif p1_card["value"] < p2_card["value"]:
        return "p2"
    return "WAR"

def create_deck() -> list[dict]:
    deck = []
    suite_options = ["H", "S", "D", "C"]
    rank_options = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    for suite in suite_options:
        for rank in rank_options:
            deck.append(create_card(rank, suite))
    return deck

def shuffle(deck: list[dict]) -> list[dict]:
    from random import randint
    for index in range(0, 100000):
        index_1 = randint(0, 51)
        index_2 = randint(0, 51)
        while index_1 == index_2:
            index_2 = randint(0, 51)
        deck[index_1], deck[index_2] = deck[index_2], deck[index_1]
    return deck
print(shuffle(create_deck()))