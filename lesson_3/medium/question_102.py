# Alan wrote the following function, which was intended to return all of the factors of number:

def factors(number):
    divisor = abs(number) # absolute value added
    result = []
    while divisor != 0: # replace '!=' with >
        if number % divisor == 0: # modulous operator outputs remainer. factors dont have remainders.
            result.append(number // divisor)
        divisor -= 1
    return result

# Alyssa noticed that this code would fail when the input is a negative number,
# and asked Alan to change the loop. How can he make this work? 
# Note that we're not looking to find the factors for negative numbers,
# but we want to handle it gracefully instead of going into an infinite loop.

print(factors(25))
print(factors(144))
print(factors(-25))
print(factors(-144))