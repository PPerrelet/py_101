# How can you determine whether a given
# string ends with an exclamation mark (!)?
# Write some code that prints True or False
# depending on whether the string ends with an exclamation mark.

STR1 = "Come over here!"  # True
STR2 = "What's up, Doc?"  # False

def test(s):
    print(s.endswith('!'))

test(STR1)
test(STR2)

print(STR1.endswith('!'))
print(STR2.endswith('!'))