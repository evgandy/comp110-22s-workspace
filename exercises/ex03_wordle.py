"""Exercise 3: Structured Wordle Game!"""

__author__ = "730227972" 

# Defining the function that scans the user's guess for characters found in the secret.


def contains_char(word: str, letter: str) -> bool: 
    """Checking for a character in the word guess."""
    assert len(letter) == 1
    i: int = 0
    correct: bool = False 
    while not correct and i < len(word): 
        if word[i] == letter: 
            correct = True 
        else:
            correct = False 
        i = i + 1
    if correct:
        return True
    else:
        return False 

# Defining the function that produces the emoji result from the inputted guess.


def emojified(guess: str, secret: str) -> str: 
    """Returning emojis based on letter matches between the guess and secret."""
    assert len(guess) == len(guess)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    a: int = 0
    result_emoji: str = ""
    while a < len(secret):
        if guess[a] == secret[a]:
            result_emoji += GREEN_BOX
        else:
            if contains_char(secret, guess[a]) is True:
                result_emoji += YELLOW_BOX
            else:
                result_emoji += WHITE_BOX
        a = a + 1
    return result_emoji


# Defining the function that ensures the user's guess is the same length as the secret word.


def input_guess(length: int) -> str: 
    """Making sure the guessed word is the correct length."""
    user_guess: str = input(f"Enter a {length} character word: ")   
    while len(user_guess) != length: 
        user_guess = input(f"That wasn't {length} chars! Try again: ")
    return user_guess 

# Defining the function that calls from the other functions to produce the main game loop. 


def main() -> None: 
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    correct: bool = False 
    turn: int = 0 
    while turn < 6 and not correct:
        print(f"===Turn {turn + 1}/6 ===")
        user_guess: str = input_guess(len(secret))
        print(emojified(user_guess, secret))
        if user_guess == secret:
            correct = True 
            print(f"You won in {turn + 1}/6 turns!")
        turn += 1
    if turn == 6:
        print("X/6 - Sorry, try again tomorrow!") 

# Making the program an accessible module. 


if __name__ == "__main__":
    main() 