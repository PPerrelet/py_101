print('Welcome to Calculator!')

print("What's the first number?") 
number1 = input()   # Ask the user for the first number.

print("What's the second number?")
number2 = input()   # Ask the user for the second number.

print('What operation would you like to perform?\n1) Add 2) Subtract 3) Multiply 4) Divide')
operator = input()  # Ask the user for an operation to perform.

if operator == '1':
    output = int(number1) + int(number2)    # Perform the operation on the two numbers.

elif operator == '2':
    output = int(number1) - int(number2)    # Perform the operation on the two numbers.

elif operator == '3':
    output = int(number1) * int(number2)    # Perform the operation on the two numbers.

elif operator == '4':
    output = int(number1) / int(number2)    # Perform the operation on the two numbers.

print(f"The result is: {output}")   # Print the result to the terminal.


