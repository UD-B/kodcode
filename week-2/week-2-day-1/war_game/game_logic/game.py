def create_player(name: str = "AI") -> dict:
    return {
        "name": name,
        "hand": [],
        "won_pile": []
    }

def init_game() -> dict:
    player_1 = create_player("UD")
    player_2 = create_player()
    deck = create_deck()
    shuffle(deck)
    player_1["hand"] = deck[:26]
    player_2["hand"] = deck[26:]
    return {
        "deck": deck,
        "player_1": player_1,
        "player_2": player_2
    }

def play_round(player_1: dict, player_2: dict) -> None:
    p1_card = player_1["hand"].pop()
    p2_card = player_2["hand"].pop()
    result = compare_cards(p1_card, p2_card)
    if result_compare == "p1":
        player_1["won_pile"].append(p1_card)
        player_1["won_pile"].append(p2_card)
    elif result_compare == "p2":
        player_2["won_pile"].append(p1_card)
        player_2["won_pile"].append(p2_card)
    return 