"""Counting letters in a string."""

__author__ = "730397999"


# Begin your solution here...

letter: str = str(input("What letter do you want to search for? "))
word: str = str(input("Enter a word: "))
i: int = 0
times_in_word: int = 0
while i < len(word):
    if word[i] == letter:
        times_in_word = times_in_word + 1
        i = i + 1 
    else:
        i = i + 1

print("Count: " + str(times_in_word)) 