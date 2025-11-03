def build_standard_deck() -> list[dict]:
    rank = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    suite = ["h", "d", "s", "c"]
    deck = []
    for i in suite:
        for j in rank:
            card = {"rank": str, "suite": str}
            card["rank"], card["suite"] = j, i
            deck.append(card)
    return deck

def shuffle_by_suite(deck: list[dict], swaps: int = 5000) -> list[dict]:
    from random import randint
    for i in range (0, 5000):
        while True:
            i = randint(0, 51)
            j = randint(0, 51)
            if i == j:
                continue
            elif deck[i]["suite"] == "H":
                if j / 5 != 0:
                    continue
            elif deck[i]["suite"] == "C":
                if j / 3 != 0:
                    continue
            elif deck[i]["suite"] == "D":
                if j / 2 != 0:
                    continue
            elif deck[i]["suite"] == "":
                if j / 7 != 0:
                    continue
            deck[i], deck[j] = deck[j], deck[i]
            break
    return deck