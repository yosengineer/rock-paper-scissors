import unittest
from unittest.mock import patch
import game

class TestRockPaperScissors(unittest.TestCase):
    def test_get_computer_choice(self):
        # Test that computer choice is valid
        for _ in range(10):
            choice = game.get_computer_choice()
            self.assertIn(choice, ['rock', 'paper', 'scissors'])

        def test_all_user_computer_combinations(self):
            outcomes = {
                ('rock', 'rock'): "It's a tie!",
                ('rock', 'paper'): "You lose!",
                ('rock', 'scissors'): "You win!",
                ('paper', 'rock'): "You win!",
                ('paper', 'paper'): "It's a tie!",
                ('paper', 'scissors'): "You lose!",
                ('scissors', 'rock'): "You lose!",
                ('scissors', 'paper'): "You win!",
                ('scissors', 'scissors'): "It's a tie!",
            }
            for user_choice in ['rock', 'paper', 'scissors']:
                for computer_choice in ['rock', 'paper', 'scissors']:
                    with self.subTest(user=user_choice, computer=computer_choice):
                        with patch('builtins.input', side_effect=[user_choice, 'exit']):
                            with patch('game.get_computer_choice', return_value=computer_choice):
                                with patch('builtins.print') as mock_print:
                                    game.play_game()
                                    mock_print.assert_any_call(outcomes[(user_choice, computer_choice)])
    @patch('builtins.input', side_effect=['rock', 'exit'])
    @patch('game.get_computer_choice', return_value='scissors')
    def test_play_game_win(self, mock_computer, mock_input):
        # Test user wins scenario
        with patch('builtins.print') as mock_print:
            game.play_game()
            mock_print.assert_any_call("You win!")

    @patch('builtins.input', side_effect=['rock', 'exit'])
    @patch('game.get_computer_choice', return_value='rock')
    def test_play_game_tie(self, mock_computer, mock_input):
        # Test tie scenario
        with patch('builtins.print') as mock_print:
            game.play_game()
            mock_print.assert_any_call("It's a tie!")

    @patch('builtins.input', side_effect=['rock', 'exit'])
    @patch('game.get_computer_choice', return_value='paper')
    def test_play_game_lose(self, mock_computer, mock_input):
        # Test user loses scenario
        with patch('builtins.print') as mock_print:
            game.play_game()
            mock_print.assert_any_call("You lose!")

    @patch('builtins.input', side_effect=['invalid', 'rock', 'exit'])
    @patch('game.get_computer_choice', return_value='scissors')
    def test_play_game_invalid_choice(self, mock_computer, mock_input):
        # Test invalid user input
        with patch('builtins.print') as mock_print:
            game.play_game()
            mock_print.assert_any_call("Invalid choice. Please try again.")

if __name__ == '__main__':
    unittest.main()
