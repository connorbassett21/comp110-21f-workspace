"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730397999"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
ONE: str = "You will finish the semester woth a 4.0 GPA!"
TWO: str = "You will meet the love of your life this semester!"
THREE: str = "You will win the lottery this week!"
FOUR: str = "UNC will win the national championship this year!"


print("Your fortune cookie says . . .")
random_integer: int = int(randint(1, 4))

if random_integer == 1:
    print(ONE)
else:
    if random_integer == 2:
        print(TWO)
    else:
        if random_integer == 3:
            print(THREE)
        else:
            print(FOUR)

print("Now, go spread positive vibes!")