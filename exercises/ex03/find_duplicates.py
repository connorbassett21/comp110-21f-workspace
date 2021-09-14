"""Finding duplicate letters in a word."""

__author__ = "730397999"

word: str = str(input("Enter a word: "))
number_of_duplicates: int = 0
duplicate: bool = False
i: int = 0
while i < len(word):
    character = word[i]
    j: int = i + 1
    while j < len(word):
        character = word[j]
        if character == word[i]:
            number_of_duplicates = number_of_duplicates + 1
        j += 1
    i += 1
if number_of_duplicates > 0:
    print("Found duplicate: True")
else:
    print("Found duplicate: False")