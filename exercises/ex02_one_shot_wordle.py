"""EX02 - One Shot Wordle"""

__author__ = "730483243"


secret_word: str = "python"
letters: int = len(secret_word)
word_input: str = input(f"What is your {letters}-letter guess? ")

while len(word_input) != len(secret_word):
    word_input: str = input(f"That was not {letters} letters! Try again: ")


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

idx: int = 0
emoji: str = ""

while idx < len(word_input):
    if str(word_input)[idx] == str(secret_word)[idx]:
        emoji += GREEN_BOX
    elif str(word_input)[idx] in secret_word:
        emoji += YELLOW_BOX
    else:
        emoji += WHITE_BOX
    idx += 1
print(emoji)


if secret_word == word_input:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")