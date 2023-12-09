from os import system
from art import logo
from random import randint
# Clear the screen for linux/Mac users, if you are on windows replace clear with cls
system('clear') 



EASY_LEVEL_DIFFICULTY = 10
HARD_LEVEL_DIFFICULTY = 5

def checkNum(guess, answer, turns):
    """check answer against guess and returns remaining turns"""

    guess = int(guess)
    if guess < answer:
        print("Too low.")
        return turns -1
                    
    elif guess > answer:
        print("Too high.")
        return turns -1

    else:
        print(f"You got it! The answer was {answer}.")

def set_difficulty():
     """Sets the number of attempts allowed"""
     level = input("Choose a difficulty. Type 'easy' or 'hard': ")
     if level == "easy":
          return EASY_LEVEL_DIFFICULTY
     else:
          return HARD_LEVEL_DIFFICULTY
    
def game():
    print(logo)
    print ("Welcome to the Number Guessing Game!")
    print ("I'm thinking of a number between 1 and 100.")
    answer = randint(1,100)
    turns = set_difficulty()
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = 0

    while guess != answer:
        guess = int(input("Make a guess: "))
        turns = checkNum(guess, answer,turns)
        print(f"You have {turns} attempts remaining to guess the number.")
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return 
        elif guess != answer:
            print("Guess again.")
keepPlaying =True     
while keepPlaying:
    play = input("Do you want to play Guess The Number?, type 'y' or 'n': ")
    if play == "y":
        system('clear')
        game()
    else:
        keepPlaying = False


             


             