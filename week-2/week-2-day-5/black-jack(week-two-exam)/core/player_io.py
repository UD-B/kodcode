def ask_player_action() -> str:
    while True:
        player_input = input("enter h to continue drawing cards or s to stop").upper()
        if player_input == "S" or player_input == "H":
            return player_input 
        print("invalid input, try again.")