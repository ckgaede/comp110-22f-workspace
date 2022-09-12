"""EX03 - The Wordle game with functions."""

__author__ = "730483243"

def contains_char(word_search: str, chr_search: str) -> bool:
    """Will determine if a chr is within a given str."""
    assert len(chr_search) == 1
    idx: int = 0
    while idx < len(word_search):
        if str((word_search)[idx]) == str(chr_search):
            return True
        idx += 1
    return False

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def emojified(secret_word: str, guess_word: str) -> str:
    """Codes for the correctly colored box."""
    assert len(guess_word) == len(secret_word)
    idx: int = 0
    emoji: str = ""
    while idx < len(guess_word):
        if contains_char(guess_word, secret_word[idx]) == True:
            if guess_word[idx] == secret_word[idx]:
                emoji += GREEN_BOX
            else:
                emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX
        idx += 1
    return(emoji)

def input_guess(expected_length: int) -> str:
    """Prompts user for an input guess of correct length."""
    guess: str = input(f"Enter a {expected_length} character word: ")    
    while len(guess) == expected_length:
        return guess
    while len(guess) != expected_length:
        guess: str = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess

def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    turns_spent: int = 1
    while turns_spent <= 6:
        print(f"=== Turn {turns_spent}/6 ===")
        guess = input_guess(5)
        print(emojified(guess, secret_word))
        if guess == secret_word:
            print(f"You won in {turns_spent}/6 turns!") 
            return None
        turns_spent += 1
    if turns_spent > 6:
        print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()