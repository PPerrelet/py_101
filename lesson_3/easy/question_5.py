# Starting with the string:
# munsters_description = "The Munsters are creepy and spooky."
# print the string with the case of all letters swapped:
#          " tHE mUNSTERS ARE CREEPY AND SPOOKY."
# That is, lowercase letters are converted to uppercase, and uppercase letters are converted to lowercase"

munsters_description = "The Munsters are creepy and spooky."
def to_lowercase(string):
    result = ''
    for letter in string:
        if letter == letter.upper():
            result += letter.lower()
        else:
            result += letter.upper()
    return result

print(to_lowercase(munsters_description)) 

# Lol its actually a built in function
print(munsters_description.swapcase())