from random import *


def guess_the_number():

    print("In this program you will guess a number between 1-100.")
    secret_number = randint(1, 100)
    guess = 0
    while guess != secret_number:
        try:
            guess = int(input("Make your guess: "))
            if guess > secret_number:
                print("Your guess is too high.")
            if guess < secret_number:
                print("Your guess is too low.")
            if guess == secret_number:
                print("You guessed the right number!")
        except ValueError:
            print("Invalid Entry, please choose a number 1 - 100.")

    print("Thank you for using my program.")
