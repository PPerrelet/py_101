import random  # Import the random module to allow random selection

# List of valid choices for the game
VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']

# Define a helper function to display messages with a consistent format
def prompt(message):
    print(f'==> {message}')  # Prefix all prompts with '==>'

# Function to display a winning message for the human
def winner():
    print('--------------------------------------------------')
    print("                The Human WINS                    ")  # human wins
    print('--------------------------------------------------')

# Function to display a winning message for the computer
def loser():
    print('--------------------------------------------------')
    print("              The Computer WINS                   ")  # comp wins
    print('--------------------------------------------------')

# Function to display a tie message
def tie():
    print('--------------------------------------------------')
    print("                   It's a Tie                     ")  # Tie
    print('--------------------------------------------------')

# Main game loop: runs indefinitely until user decides to stop
while True:
    # Ask the user for their choice
    prompt(f"Choose one: {', '.join(VALID_CHOICES)}")  # Display valid choices
    human_choice = input().lower()  # Make user input lowercase

    # Validate user input; repeat until a valid choice is made
    while human_choice not in VALID_CHOICES:
        prompt("That's not a valid choice")  # Notify of invalid input
        human_choice = input().lower()  # Retry input

    # Randomly choose for the computer
    computer_choice = random.choice(VALID_CHOICES)

    # Show what both players chose
    prompt(f'Human chose {human_choice}')
    prompt(f'Computer chose {computer_choice}')

    # Determine winner:
    # Rock beats Scissors, Scissors beats Paper, Paper beats Rock
    # Rock beats Lizard, Lizard beats Spock, Spock beats Scissors
    # Scissors beats Lizard, Lizard beats Paper, Paper beats Spock,
    # Spock beats rock
    if ((human_choice == 'rock' and computer_choice == 'scissors') or
        (human_choice == 'paper' and computer_choice == 'rock') or
        (human_choice == 'scissors' and computer_choice == 'paper') or 
        (human_choice == 'rock' and computer_choice == 'lizard') or 
        (human_choice == 'lizard' and computer_choice == 'spock') or 
        (human_choice == 'spock' and computer_choice == 'scissors') or
        (human_choice == 'scissors' and computer_choice == 'lizard') or
        (human_choice == 'lizard' and computer_choice == 'paper') or 
        (human_choice == 'paper' and computer_choice == 'spock') or 
        (human_choice == 'spock' and computer_choice == 'rock')):
        winner()  # Human wins
    elif ((computer_choice == 'rock' and human_choice == 'scissors') or
          (computer_choice == 'paper' and human_choice == 'rock') or
          (computer_choice == 'scissors' and human_choice == 'paper') or
          (computer_choice == 'rock' and human_choice == 'lizard') or 
          (computer_choice == 'lizard' and human_choice == 'spock') or 
          (computer_choice == 'spock' and human_choice == 'scissors') or
          (computer_choice == 'scissors' and human_choice == 'lizard') or
          (computer_choice == 'lizard' and human_choice == 'paper') or 
          (computer_choice == 'paper' and human_choice == 'spock') or 
          (computer_choice == 'spock' and human_choice == 'rock')):
        loser()  # Computer wins
    else:
        tie()  # If none of the above, it's a tie

    # Ask the user if they want to play again
    prompt('Do you wish to play again, mortal? (y/n)')
    answer = input().lower()  # Normalize response

    # Validate yes/no answer
    while True:
        if answer.startswith('n') or answer.startswith('y'):
            break  # Valid input; exit loop
        prompt("Please enter 'y' or 'n'.")  # Ask again if invalid
        answer = input().lower()

    # Exit game if user said no
    if answer[0] == 'n':
        prompt("Farewell, brave mortal!")  # goodbye message
        break  # Exit main game loop