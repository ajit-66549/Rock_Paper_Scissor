import random

def get_user_choice():
    """
    Prompt the user to enter their choice.

    Returns:
        str: The user's choice, converted to lowercase.
    """
    choice = input("Enter your choice: ").lower()
    return choice

def is_valid_input(user_choice, choices):
    """
    Check whether the user's choice is valid.

    Args:
        user_choice (str): The choice entered by the user.
        choices (list): A list of valid choices.

    Returns:
        bool: True if the input is valid, False otherwise.
    """
    return user_choice in choices

def winner(random_choice, user_choice):
    """
    Determine and print the winner of the game.

    Args:
        random_choice (str): The choice made by the computer.
        user_choice (str): The choice made by the user.

    Returns:
        None
    """
    if random_choice == user_choice:
        print("Game draw")
    elif ((random_choice == 'rock' and user_choice == 'scissor') or
          (random_choice == 'paper' and user_choice == 'rock') or
          (random_choice == 'scissor' and user_choice == 'paper')):
        print("Result: Computer won the game")
    else:
        print("Result: You won the game")

def game(ask_user):
    """
    Run the rock-paper-scissors game loop until the user quits.

    Args:
        ask_user (str): The user's initial response to start the game.

    Returns:
        None
    """
    while ask_user != 'quit':
        choices = ['rock', 'paper', 'scissor']
        random_choice = random.choice(choices)
        user_choice = get_user_choice()
        
        if is_valid_input(user_choice, choices):
            print(f"\nYou chose: {user_choice}\nComputer chose: {random_choice}\n")
            winner(random_choice, user_choice)
        else:
            print("Please enter a valid choice.")
            continue
            
        ask_user = input("Press any key to continue. If not, type 'quit': ").lower()
        
    print("Thank you for playing!")


ask_user = input("Do you want to play the game? (yes/no): ").lower()
if ask_user == 'yes':
    game(ask_user)
else:
    print("No worries! See you next time.\nHave a great time!")