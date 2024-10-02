import random

def get_computer_choice():
    """Generate random choice for computer: rock, paper, or scissors."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_winner(user_choice, computer_choice):
    """Determine the winner between the user and the computer."""
    if user_choice == computer_choice:
        return "It's a tie!"
    
    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'scissors' and computer_choice == 'paper') or \
       (user_choice == 'paper' and computer_choice == 'rock'):
        return 'You win!'
    
    return 'Computer wins!'

def play_game():
    """Play a round of Rock-Paper-Scissors."""
    user_score = 0
    computer_score = 0
    
    while True:
        
        user_choice = input("Choose rock, paper, or scissors (or type 'quit' to exit): ").lower()
        
        if user_choice == 'quit':
            print("Thanks for playing!")
            break
        
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please try again.")
            continue
        
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        
        result = get_winner(user_choice, computer_choice)
        print(result)
        
        
        if "You win" in result:
            user_score += 1
        elif "Computer wins" in result:
            computer_score += 1
        
        # Display scores
        print(f"Score: You - {user_score} | Computer - {computer_score}")
        
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Final Score: You -", user_score, "| Computer -", computer_score)
            print("Goodbye!")
            break

if __name__ == "__main__":
    play_game()
