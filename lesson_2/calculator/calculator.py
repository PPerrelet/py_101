import json

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

prompt(MESSAGES['select_code'])
prompt(MESSAGES['language_codes'])
language = input()
while language not in ["en", "tl", "fr"]:
    prompt(MESSAGES['language_error'])
    language = input()

while True:
    prompt(MESSAGES[language]['welcome'])
    prompt(MESSAGES[language]['first_number'])
    number1 = input()

    while invalid_number(number1):
        prompt(MESSAGES[language]['invalid_number'])
        number1 = input()

    prompt(MESSAGES[language]['second_number'])
    number2 = input()

    while invalid_number(number2):
        prompt(MESSAGES[language]['invalid_number'])
        number2 = input()

    prompt(MESSAGES[language]['operator_prompt'])
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt(MESSAGES[language]['operator_error'])
        operation = input()

    match operation:
        case "1":
            output = float(number1) + float(number2)
        case "2":
            output = float(number1) - float(number2)
        case "3":
            output = float(number1) * float(number2)
        case "4":
            output = float(number1) / float(number2)

    prompt(f"{MESSAGES[language]['result']} {output}")
    prompt(MESSAGES[language]['repeat_operation'])
    answer = input()
    if answer and answer[0].lower() != 'y':
        break