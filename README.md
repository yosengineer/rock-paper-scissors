# Rock, Paper, Scissors Game

## Overview
This is a simple command-line implementation of the classic Rock, Paper, Scissors game in Python. You play against the computer, and the game continues until you choose to exit.

## How to Play
1. Run the game using Python:
   ```
   python game.py
   ```
2. Enter your choice: `rock`, `paper`, or `scissors` when prompted.
3. The computer will randomly select its choice.
4. The winner is determined by the following rules:
   - Rock beats Scissors
   - Scissors beats Paper
   - Paper beats Rock
   - If both choices are the same, it's a tie
5. After each round, you can choose to play again or exit the game.

## Game Rules
- **Rock** crushes **Scissors**
- **Scissors** cut **Paper**
- **Paper** covers **Rock**
- If both you and the computer choose the same, it's a tie

## Example
```
Welcome to Rock, Paper, Scissors!
Enter your choice (rock, paper, scissors) or 'exit' to quit: rock
Computer chose: scissors
You win!
Do you want to play again? (yes/no): no
Thanks for playing! Goodbye!
```

## Automated Testing
Unit tests are provided in `test_game.py` and can be run with:
```
python -m unittest discover
```

## License
This project is for educational purposes.
