"""One Shot Wordle!"""

__author__ = "730227972" 

# Establishing starting variables. 

secret_word: str = "python" 

length_secret: int = len(secret_word)

guess_str: str = str(input(f"What is your {length_secret}-letter guess? "))

guess_int: int = len(guess_str)

# Making sure guess has the correct number of letters. 

while guess_int != (len(secret_word)): 
    guess_str: str = str(input(f"That was not {length_secret} letters! Try again: "))
    guess_int: int = len(guess_str) 

# Initializing named constants. 

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# Initializing variables needed for checking indices. 

index_int: int = 0

result_emoji: str = ""

index_guess: str = str(guess_str[index_int]) 

index_secret: str = str(secret_word[index_int])

# Loop that checks indices for correct matches. 

while index_int < len(secret_word):
    if index_guess == index_secret:
        result_emoji: str = str(f"{result_emoji}{GREEN_BOX}") 
    else:
        alt_index: int = 0 
        match: bool = False 
        alt_index_secret: str = str(secret_word[alt_index])
        while alt_index < len(secret_word):
            if index_guess == alt_index_secret:
                match: bool = True 
            alt_index: int = alt_index + 1
            if alt_index <= (len(secret_word) - 1):
                alt_index_secret: str = str(secret_word[alt_index])
        if not match:
            result_emoji: str = str(f"{result_emoji}{WHITE_BOX}")
        else: 
            result_emoji: str = str(f"{result_emoji}{YELLOW_BOX}") 

    index_int: int = index_int + 1
    if index_int <= (len(secret_word) - 1):
        index_guess: str = str(guess_str[index_int])
        index_secret: str = str(secret_word[index_int])

# Printing results of checked indices. 

print(result_emoji) 

# Printing result of game.

if guess_str == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
