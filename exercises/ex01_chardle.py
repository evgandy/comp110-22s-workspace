"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730227972"

word_5: str = str(input("Enter a 5-character word: "))

if len(word_5) != 5:
    exit(print("Error: Word must contain 5 characters"))

character_1: str = str(input("Enter a single character: "))

if len(character_1) != 1:
    exit(print("Error: Character must be a single character."))

print("Searching for " + character_1 + " in " + word_5)

matching_indices: int = 0 

if character_1 == word_5[0]:
    print(character_1 + " found at index 0")
    matching_indices = matching_indices + 1

if character_1 == word_5[1]:
    print(character_1 + " found at index 1")
    matching_indices = matching_indices + 1 

if character_1 == word_5[2]:
    print(character_1 + " found at index 2")
    matching_indices = matching_indices + 1 

if character_1 == word_5[3]:
    print(character_1 + " found at index 3")
    matching_indices = matching_indices + 1

if character_1 == word_5[4]:
    print(character_1 + " found at index 4")
    matching_indices = matching_indices + 1 

if matching_indices == 0:
    print("No instances of " + character_1 + " found in " + word_5) 
else:
    if matching_indices == 1:
        print("1 instance of " + character_1 + " found in " + word_5) 
    else:
        print(str(matching_indices) + " instances of " + character_1 + " found in " + word_5) 
