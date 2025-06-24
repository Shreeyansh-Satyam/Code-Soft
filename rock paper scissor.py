import random

def get_user_choice():
    choices = ['rock', 'paper', 'scissors']
    while True:
        choice = input("Choose rock, paper, or scissors (or 'exit' to quit): ").lower()
        if choice in choices:
            return choice
        if choice == 'exit':
            return None
        print("Invalid choice. Try again.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, comp):
    wins = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }
    if user == comp:
        return 'tie'
    elif wins[user] == comp:
        return 'user'
    else:
        return 'computer'

def play():
    user_score = comp_score = 0
    while True:
        user = get_user_choice()
        if user is None:
            break
        comp = get_computer_choice()
        print(f"You chose {user}, computer chose {comp}.")
        result = determine_winner(user, comp)
        if result == 'tie':
            print("It's a tie! 🤝")
        elif result == 'user':
            print("You win! 🎉")
            user_score += 1
        else:
            print("Computer wins! 💻")
            comp_score += 1
        print(f"Score — You: {user_score} | Computer: {comp_score}\n")

    print("Thanks for playing!")
    print(f"Final score — You: {user_score}, Computer: {comp_score}")

if __name__ == "__main__":
    play()
