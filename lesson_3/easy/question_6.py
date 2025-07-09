# Determine whether the name Dino appears in the strings below -- check each string separately:
str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."

sub = 'Dino'

def function(string):
    if sub in string:
        print('Dino is found')
    else:
        print('Dino is not found')

function(str1)
function(str2)

# or

'Dino' in str1  # False
'Dino' in str2  # True