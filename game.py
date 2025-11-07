# Create a simple rock, paper, scissors game
# Provide a welcome message
# Get the user's choice
# Get the computer's choice
# Compare the two choices
# Print the results
# Ask the user if they want to play again
# Say goodbye when they choose to exit and end the game
# Use one function for the game logic and another for getting the computer's choice

import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors) or 'exit' to quit: ").lower()
        
        if user_choice == 'exit':
            print("Thanks for playing! Goodbye!")
            break
        
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please try again.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print("You win!")
        else:
            print("You lose!")
            
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    play_game()