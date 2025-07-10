# What is the output of the following code?

answer = 42

def mess_with_it(some_number):
    return some_number + 8

new_answer = mess_with_it(answer)

print(answer - 8)  # answer still equals 42
                   # new_answer is the result of the mess_with_it function.