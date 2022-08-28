"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730483243"


word_input: str = input("Enter a 5-character word: ")

if len(word_input) == 5:
    letter_input: str = input("Enter a single character: ")
    if len(letter_input) == 1:
        print("Searching for " + letter_input + " in " + word_input)
    else:
        print("Error: Character must be a single character.")
        exit()
else:
    print("Error: Word must contain 5 characters")
    exit()


counting: int = 0

if letter_input == (word_input)[0]:
    print(letter_input, "found at index 0")
    counting = counting + 1
if letter_input == (word_input)[1]:
    print(letter_input, "found at index 1")
    counting = counting + 1
if letter_input == (word_input)[2]:
    print(letter_input, "found at index 2")
    counting = counting + 1
if letter_input == (word_input)[3]:
    print(letter_input, "found at index 3")
    counting = counting + 1
if letter_input == (word_input)[4]:
    print(letter_input, "found at index 4")
    counting = counting + 1

if counting >= int(1):
    if counting == int(1):
        print(counting, "instance of",letter_input, "found in", word_input)
    else:
        print(counting, "instances of",letter_input, "found in", word_input)
else:
    print("No instances of",letter_input, "found in", word_input)