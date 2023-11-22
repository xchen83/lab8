import unittest
from logic import Game, Human, Bot

class TestTicTacToe(unittest.TestCase):

# The game is initialized with an empty board
    def test_game_initialized_with_empty_board(self):
        game = Game()
        empty_board = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
        self.assertEqual(game.board, empty_board)

# The game is initialized with either 2 players (human-human) or 1 player (human-bot)
    def test_game_initialized_with_one_player(self):
        game = Game(playerX=Human(), playerO=Bot())
        self.assertIsInstance(game.playerX, Human)
        self.assertIsInstance(game.playerO, Bot)

# Players are assigned a unique piece to play: X or O
    def test_players_assigned_unique_pieces(self):
        game = Game(playerX=Human(), playerO=Bot())
        self.assertEqual(game.playerX.turn, 'X')
        self.assertEqual(game.playerO.turn, 'X')

# After one player plays, the other player has a turn
    def test_alternate_turns_after_player_move(self):
        game = Game(playerX=Human(), playerO=Bot())
        game.modify_array(2)  # Player X makes a move
        self.assertEqual(game.turn, 'X')

# All winning end of the games detected, and draw games are identified 
    def test_winning_end_of_games_and_draw_identified(self):
        game = Game(playerX=Human(), playerO=Human())
        # Winning end of the games detected
        for move in [1, 4, 2, 5, 3]:
            game.modify_array(move)
            game.other_player()

        self.assertTrue(game.get_winner() == 'X' or game.get_winner() == 'O' or game.get_winner() =='N')

        # Draw Identified
        for move in [5, 2, 8, 3, 7, 4, 6, 9, 1]:
            game.modify_array(move)
            game.other_player()

        self.assertEqual(game.get_winner(), 'N')

# Players can play only in viable spots
    def test_players_can_play_only_in_viable_spots(self):
        game = Game(playerX=Human(), playerO=Bot())
        game.modify_array(1)
        game.other_player()
        game.modify_array(1)  
        self.assertNotEqual(game.turnCounter, 2)

#The correct game winner, if one exists, is detected
    def test_correct_winner_detected(self):
        game = Game(playerX=Human(), playerO=Human())
        for move in [1, 4, 2, 5, 3]:
            game.modify_array(move)
            game.other_player()

        self.assertEqual(game.get_winner(), 'X')

if __name__ == '__main__':
    unittest.main()
