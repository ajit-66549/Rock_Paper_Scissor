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
    if random_choice == user_choice:
        print("Round draw")
        return "draw"
    elif ((random_choice == 'rock' and user_choice == 'scissor') or
          (random_choice == 'paper' and user_choice == 'rock') or
          (random_choice == 'scissor' and user_choice == 'paper')):
        return "computer"
    else:
        return "user"

def game(rounds):
    """
    Runs a game of Rock-Paper-Scissors for a specified number of rounds.

    This function manages the game loop, keeps track of scores for both the user
    and the computer, and determines the winner.

    Args:
        rounds (int): The total number of rounds to be played in the game.

    Returns:
        None: This function prints the game's progress, round results,
              final scores, and the overall winner.
    """
    user_score, com_score = 0, 0
    round = 1
    while round <= rounds:
        print(f"\n--- Round {round}/{rounds} ---")
        choices = ['rock', 'paper', 'scissor']
        random_choice = random.choice(choices)
        user_choice = get_user_choice()
        
        if is_valid_input(user_choice, choices):
            print(f"\nYou chose: {user_choice}\nComputer chose: {random_choice}\n")
            win = winner(random_choice, user_choice)
            if (win == "user"):
                user_score = user_score + 1
            elif (win == "computer"):
                com_score = com_score + 1
            else:
                user_score = user_score + 1
                com_score = com_score + 1
            round += 1
        else:
            print("Please enter a valid choice.")
            continue
        if round <= rounds: 
            input("\nPress Enter to continue to the next round...")
    
    print(f"Your Score: {user_score}\nComputer Score: {com_score}")
    
    if (user_score > com_score):
        print("You won the game\n")
    else:
        print("Computer won the game\n")
        
    print("\nThank you for playing!")


ask_user = input("Do you want to play the game? (yes/no): ").lower()
if ask_user == 'yes':
    rounds = int(input("How many rounds you want to play?[3 or 5] "))
    game(rounds)
else:
    print("No worries! See you next time.\nHave a great time!")