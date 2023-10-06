import random

def get_user_choice():
    choice = input("Choose Rock, Paper, or Scissors: ")
    return choice.lower()

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == 'rock':
        return "You win!" if computer_choice == 'scissors' else "Computer wins!"
    elif user_choice == 'paper':
        return "You win!" if computer_choice == 'rock' else "Computer wins!"
    elif user_choice == 'scissors':
        return "You win!" if computer_choice == 'paper' else "Computer wins!"
    else:
        return "Invalid input. Please choose Rock, Paper, or Scissors."

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose {user_choice.capitalize()}.")
    print(f"The computer chose {computer_choice.capitalize()}.")
    result = determine_winner(user_choice, computer_choice)
    print(result)

play_game()
