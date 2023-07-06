from random import randint
from guess_number import logo



easy_attempts = 10
hard_attempts = 5

def check_answer(guess, answer, turns):
    if guess > answer:
        print("Your guess is too high.")
        return turns - 1
    elif guess < answer:
        print("Your guess is too low.")
        return turns - 1
    else:
        print(f"The random number was {answer}!")

def set_difficulty():
    level = input("What mode would you like to play? Type 'easy' or 'hard'. ")
    if level == "easy":
        return easy_attempts
    else:
        return hard_attempts

def game():
    print(logo)
     #Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    turns = set_difficulty()
    guess = 0

    while guess != answer:
        print(f"You have this many {turns} left.")
        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You have no more guesses left, you lose!")
            return
        elif guess != answer:
            print("Guess again.")

game()