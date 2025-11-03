from .player_io import ask_player_action as ask
def calculate_hand_value(hand: list[dict]) -> int:
    calculated_value = 0
    for i in hand:
        rank_value = 0
        if i["rank"] == "A":
            rank_value = 1
        elif i["rank"] == "2":
            rank_value = 2
        elif i["rank"] == "3":
            rank_value = 3
        elif i["rank"] == "4":
            rank_value = 4
        elif i["rank"] == "5":
            rank_value = 5
        elif i["rank"] == "6":
            rank_value = 6
        elif i["rank"] == "7":
            rank_value = 7
        elif i["rank"] == "8":
            rank_value = 8
        elif i["rank"] == "9":
            rank_value = 9
        elif i["rank"] == "10":
            rank_value = 10
        elif i["rank"] == "J":
            rank_value = 10
        elif i["rank"] == "Q":
            rank_value = 10
        elif i["rank"] == "K":
            rank_value = 10
        calculated_value += rank_value
    return calculated_value

def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    player["hand"].append(deck.pop(0))
    player["hand"].append(deck.pop(0))
    dealer["hand"].append(deck.pop(0))
    dealer["hand"].append(deck.pop(0))
    return None

def dealer_play(deck: list[dict], dealer: dict) -> bool:
    dealer_calc = calculate_hand_value(dealer["hand"])
    while dealer_calc <= 17:
        dealer["hand"].append(deck.pop(0))
        dealer_calc = calculate_hand_value(dealer["hand"])
    if dealer_calc > 21:
        return False
    else:
        return True
    
def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    deal_two_each(deck, player, dealer)
    print(f"your hand is {player["hand"]}")
    player_hand = calculate_hand_value(player["hand"])
    while True:
        player_input = ask()
        if player_input == "H":
            player["hand"].append(deck.pop(0))
            player_hand = calculate_hand_value(player["hand"])
            print(f"your hand amounts to {player_hand}")
            if player_hand > 21:
                print("you lose")
                print(f"your hand amounts to {player_hand}")
                break
            elif player_hand <= 21:
                continue
        elif player_input == "S":
            dealer_win = dealer_play(deck, dealer)
            if not dealer_win:
                break
            elif dealer_win:
                calculated_dealer_hand = calculate_hand_value(dealer["hand"])
                if calculated_dealer_hand > player_hand:
                    print("you lose")
                    print(f"your hand {player_hand} dealer hand {calculated_dealer_hand}")
                    break
                elif calculated_dealer_hand < player_hand:
                    print("you win")
                    print(f"your hand {player_hand} dealer hand {calculated_dealer_hand}")
                    break
                elif calculated_dealer_hand == player_hand:
                    print("draw")
                    print(f"your hand {player_hand} dealer hand {calculated_dealer_hand}")
                    break