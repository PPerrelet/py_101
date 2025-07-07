import json

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        number = float(number_str)
        if number <= 0:
            raise ValueError(f"Value must be > 0: {number_str}")
    except ValueError:
        return True

    return False

with open('clc_messages.json', 'r') as file:
    MESSAGES = json.load(file)

prompt(MESSAGES['select_code'])
prompt(MESSAGES['language_codes'])
language = input()
while language not in ["en", "tl", "fr"]:
    prompt(MESSAGES['language_error'])
    language = input()

prompt("---------------------------------")
prompt(MESSAGES[language]['welcome'])

while True:
    prompt("---------------------------------")

    prompt(MESSAGES[language]['loan_amount'])

    amount = input()
    while invalid_number(amount):
        prompt(MESSAGES[language]['invalid_number'])
        amount = input()

    prompt(MESSAGES[language]['interest_rate'])

    interest_rate = input()

    while invalid_number(interest_rate):
        prompt(MESSAGES[language]['invalid_number'])
        interest_rate = input()

    prompt(MESSAGES[language]['loan_duration'])
    months = input()

    while invalid_number(months):
        prompt(MESSAGES[language]['invalid_number'])
        months = input()

    monthly_interest_rate = (float(interest_rate) / 100) / 12
    months = float(months)
    loan_amount = float(amount)

    monthly_payment = loan_amount * (
        monthly_interest_rate /
          (1 -(1 + monthly_interest_rate) ** (-months))
    )
    prompt("---------------------------------")
    prompt(
    MESSAGES[language]['monthly_payment_msg'].format(
        monthly_payment_msg=monthly_payment
    )
)

    prompt("---------------------------------")
    prompt(MESSAGES[language]['repeat_calculation'])
    prompt(MESSAGES[language]['repeat_answer'])
    answer = input().lower()
    while True:
        if answer.startswith('y') or answer.startswith('n') :
            break

    if answer[0] == 'n':
        prompt("---------------------------------")
        prompt(MESSAGES[language]['farewell'])
        prompt("---------------------------------")
        break