# Using the following string, print a string that contains the same value,
# but using all lowercase letters except for the first character, 
# which should be capitalized.

munsters_description = "the Munsters are CREEPY and Spooky."
# => 'The munsters are creepy and spooky.'

munsters_description = munsters_description.lower()

print(munsters_description[0].upper() + munsters_description[1:].lower())
print(munsters_description.capitalize())

