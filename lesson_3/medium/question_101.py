# Let's do some "ASCII Art": a stone-age form of nerd artwork from back in the days before computers had video screens.

# For this practice problem, write a program that outputs The Flintstones Rock! 10 times,
# with each line prefixed by one more hyphen than the line above it. The output should start out like this:

string = 'The Flintstones Rock!'

string = 'The Flintstones Rock!'

def tenx(string):
    for prompt in range(1, 11):
        print('-' * prompt + string)

tenx(string)
