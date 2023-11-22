from logic import Game, Human, Bot

if __name__ == '__main__':
    game = Game()
    human_player = Human()
    bot_player = Bot()

    print("Welcome to Tic-Tac-Toe!")

    while not game.leaveLoop:
        game.print_board()
        if game.turnCounter % 2 == 0:
            number_picked = human_player.make_move()
            game.modify_array(number_picked)
        else:
            other_player_choice = bot_player.make_move()
            print("\nOther Player's Choice:", other_player_choice)
            game.modify_array(other_player_choice)

        winner = game.get_winner()
        if winner != "N":
            game.print_board()
            print(f"{winner} won!")
            break
        elif game.turnCounter == 9:
            game.print_board()
            print("It's a draw!")
            break

        game.other_player()
        game.turnCounter += 1
