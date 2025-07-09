# Starting with the string:
famous_words = "seven years ago..."
# Show two different ways to create a
# new string with "Four score and "
# prepended to the front of the string referenced by famous_words.

quote1 = 'Four score and ' + famous_words
print(quote1)
quote2 = f'Four score and ' + {famous_words}
print(quote2)