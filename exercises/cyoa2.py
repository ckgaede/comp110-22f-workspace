"""Choose Your Own Adventure experience."""

from random import randint
points: int = 0

def main() -> None:
    global points
    greet()
    game_start: str = input("Choose a pathway. Enter 1 to end. Enter 2 to start guessing. Enter 3 for a challenge! ")
    if game_start == "1":
        print(f"Game over. You have {points} total points. ")
    elif game_start == "2":
        print("You have unlimited guesses to guess a number from 1-50. Guesses that are within +5 or -5 of the mystery number will be +1 point. Guesses outside of that range will be -1 point. Correctly guessing the mystery number will be +5 points. Good luck! ")
        guess: int = input("Enter a guess between 1 and 50. ")
        guessing_normal(guess)
        print(guessing_normal)
        main()
    elif game_start == "3":
        print("DIRECTIONS################")
        points = points + guessing_challenge(points)
        main()






def greet() -> None:
    player: str = input("What is your name? ")
    greeting: str = (f"Welcome to the CYOA Game, {player}! In this game, you will be trying to guess a random number.")
    print(greeting)


def guessing_normal(guess: int) -> None:
    global points
    mystery: int = randint(1, 50)
    print(mystery)
    while guess != int(mystery):
        if int(mystery - 5) <= int(guess) <= int(mystery + 5):
            points += 1
            print(f"You ARE within +5 or -5 of the mystery number! +1 point. You have {points} total point(s). ")
        else:
            points -= 1
            print(f"You are NOT within +5 or -5 of the mystery number! -1 point. You have {points} total point(s). ")
        guess = int(input("Enter a number between 1 and 50. "))
    points += 5
    print(f"GAME OVER! You got it! {mystery} was the mystery number! +5 points. You have {points} total point(s). Now, you'll enter your name again to choose from the original options. ")


        

def guessing_challenge(points: int) -> int: 
    if points != 0:
        local_points: int = 0
        multiplier: int = abs(int(input("Enter a number from 1-5 to increase your bounds for a challenge! ")))
        new_bound: int = (50 * multiplier)
        mystery_challenge: int = randint(1, int(new_bound))
        print(mystery_challenge)
        guess_challenge: int = input(f"Enter a number between 1 and {new_bound}. ")
        while guess_challenge != int(mystery_challenge):
            if int(mystery_challenge - 5) <= int(guess_challenge) <= int(mystery_challenge + 5):
                local_points += 1
                print(f"You ARE within +5 or -5 of the mystery number! +1 point. You have {local_points} challenge point(s). ")
            else:
                local_points -= 1
                print(f"You are NOT within +5 or -5 of the mystery number! -1 point. You have {local_points} challenge point(s). ")
            guess_challenge = int(input(f"Enter a number between 1 and {new_bound}. "))
        local_points += 5
        print(f"GAME OVER! You got it! {mystery_challenge} was the mystery number! +5 points. You have {local_points} challenge point(s). Now, you'll enter your name again to choose from the original options. ")
        return(local_points)
    else:
        print("Before you try a challenge, start over and try starting with a normal guessing game. ")
        return 0
    


    



if __name__ == "__main__":
    main()

