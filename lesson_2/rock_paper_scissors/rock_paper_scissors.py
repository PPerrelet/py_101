import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']

WINNING_COMBOS = {
    'rock':     ['scissors', 'lizard'],
    'paper':    ['rock',     'spock'],
    'scissors': ['paper',    'lizard'],
    'lizard':   ['paper',    'spock'],
    'spock':    ['rock',     'scissors'],
}

ACTIONS = {
    ('rock', 'scissors'):     'Rock crushes Scissors',
    ('rock', 'lizard'):       'Rock crushes Lizard',
    ('paper', 'rock'):        'Paper covers Rock',
    ('paper', 'spock'):       'Paper disproves Spock',
    ('scissors', 'paper'):    'Scissors cuts Paper',
    ('scissors', 'lizard'):   'Scissors decapitates Lizard',
    ('lizard', 'paper'):      'Lizard eats Paper',
    ('lizard', 'spock'):      'Lizard poisons Spock',
    ('spock', 'scissors'):    'Spock smashes Scissors',
    ('spock', 'rock'):        'Spock vaporizes Rock',
}

def player_wins(player_choice, computer_choice):
    return computer_choice in WINNING_COMBOS[player_choice]

def comp_wins(computer_choice, player_choice):
    return player_choice in WINNING_COMBOS[computer_choice]

def prompt(message):
    print(f'==> {message}')

while True:
    HUMAN_WINS = 0
    COMPUTER_WINS = 0

    while HUMAN_WINS < 3 and COMPUTER_WINS < 3:
        candidates = VALID_CHOICES[:]
        NEXT_LETTERS = ""

        while True:
            prompt(f"Choose one: {', '.join(candidates)}")

            if NEXT_LETTERS and len(candidates) > 1:
                prompt("Multiple matches found. Please enter the next letter.")

            letter = input().lower()
            NEXT_LETTERS += letter

            candidates = [
                word for word in candidates if word.startswith(NEXT_LETTERS)
            ]

            if not candidates:
                prompt("No matches found. Starting over.")
                candidates = VALID_CHOICES[:]
                NEXT_LETTERS = ""
            elif len(candidates) == 1:
                human_choice = candidates[0]
                break

        comp_choice = random.choice(VALID_CHOICES)

        prompt(f'Human chose {human_choice} and Computer chose {comp_choice}')

        if player_wins(human_choice, comp_choice):
            action = ACTIONS[(human_choice, comp_choice)]
            prompt(f'{action}! You win this round.')
            HUMAN_WINS += 1
        elif comp_wins(comp_choice, human_choice):
            action = ACTIONS[(comp_choice, human_choice)]
            prompt(f'{action}! Computer wins this round.')
            COMPUTER_WINS += 1
        else:
            prompt("Both chose the same. It's a tie!")

        print(
         '--------------------------------------------------\n'
          f'            Human: {HUMAN_WINS} | Computer: {COMPUTER_WINS}\n'
         '--------------------------------------------------'
    )

    if HUMAN_WINS == 3:
        prompt("The Human conquers with 3 wins!")
    else:
        prompt("The Computer triumphs with 3 wins!")

    prompt('Do you wish to play again, mortal? (y/n)')
    answer = input().lower()

    while not answer.startswith('y') and not answer.startswith('n'):
        prompt("Please enter 'y' or 'n'.")
        answer = input().lower()

    if answer.startswith('n'):
        prompt("Farewell, brave mortal!")
        break
