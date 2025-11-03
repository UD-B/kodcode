def create_card(rank: str, suite: str) -> dict:
    urank = rank.upper()
    usuite = suite.upper()
    match urank:
        case "2":
            imprint = {"2": 2}
        case "3":
            imprint = {"3": 3}
        case "4":
            imprint = {"4": 4}
        case "5":
            imprint = {"5": 5}
        case "6":
            imprint = {"6": 6}
        case "7":
            imprint = {"7": 7}
        case "8":
            imprint = {"8": 8}
        case "9":
            imprint = {"9": 9}
        case "10":
            imprint = {"10": 10}
        case "J":
            imprint = {"J": 11}
        case "Q":
            imprint = {"Q": 12}
        case "K":
            imprint = {"K": 13}
        case "A":
            imprint = {"A": 14}
    card = {"rank": "", "suite": "", "value": 0}
    card["suite"] = usuite
    for k, v in imprint.items():
        card["rank"], card["value"] = k, v
        break
    return card



def compare_cards(p1_card: dict, p2_card: dict) -> str:
    winner = ""
    if p1_card["value"] > p2_card["value"]:
        winner = "p1"
    elif p1_card["value"] < p2_card["value"]:
        winner = "p2"
    elif p1_card["value"] == p2_card["value"]:
        winner = "WAR"
    return winner

def create_deck() -> list[dict]:
    deck = []
    deck.append(create_card("2", "H"))
    deck.append(create_card("3", "H"))
    deck.append(create_card("4", "H"))
    deck.append(create_card("5", "H"))
    deck.append(create_card("6", "H"))
    deck.append(create_card("7", "H"))
    deck.append(create_card("8", "H"))
    deck.append(create_card("9", "H"))
    deck.append(create_card("10", "H"))
    deck.append(create_card("J", "H"))
    deck.append(create_card("Q", "H"))
    deck.append(create_card("K", "H"))
    deck.append(create_card("A", "H"))
    deck.append(create_card("2", "C"))
    deck.append(create_card("3", "C"))
    deck.append(create_card("4", "C"))
    deck.append(create_card("5", "C"))
    deck.append(create_card("6", "C"))
    deck.append(create_card("7", "C"))
    deck.append(create_card("8", "C"))
    deck.append(create_card("9", "C"))
    deck.append(create_card("10", "C"))
    deck.append(create_card("J", "C"))
    deck.append(create_card("Q", "C"))
    deck.append(create_card("K", "C"))
    deck.append(create_card("A", "C"))
    deck.append(create_card("2", "D"))
    deck.append(create_card("3", "D"))
    deck.append(create_card("4", "D"))
    deck.append(create_card("5", "D"))
    deck.append(create_card("6", "D"))
    deck.append(create_card("7", "D"))
    deck.append(create_card("8", "D"))
    deck.append(create_card("9", "D"))
    deck.append(create_card("10", "D"))
    deck.append(create_card("J", "D"))
    deck.append(create_card("Q", "D"))
    deck.append(create_card("K", "D"))
    deck.append(create_card("A", "D"))
    deck.append(create_card("2", "S"))
    deck.append(create_card("3", "S"))
    deck.append(create_card("4", "S"))
    deck.append(create_card("5", "S"))
    deck.append(create_card("6", "S"))
    deck.append(create_card("7", "S"))
    deck.append(create_card("8", "S"))
    deck.append(create_card("9", "S"))
    deck.append(create_card("10", "S"))
    deck.append(create_card("J", "S"))
    deck.append(create_card("Q", "S"))
    deck.append(create_card("K", "S"))
    deck.append(create_card("A", "S"))
    return deck

def shuffle(deck: list[dict]) -> list[dict]:
    from random import randint
    for i in range(0, 1000):
        index1 = randint(0, 51)
        index2 = randint(0, 51)
        while index1 == index2:
            index2 = randint(0, 51)
        deck[index1], deck[index2] = deck[index2], deck[index1]
    return deck