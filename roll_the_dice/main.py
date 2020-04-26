from random import *


def roll_the_dice():
    print("This program is going to be like rolling two dice. It will show you two random numbers.")
    reply = 'y'
    while reply == 'y':
        die_1 = randint(1, 6)
        print("Die One: " + str(die_1))

        die_2 = randint(1, 6)
        print("Die Two: " + str(die_2))

        dice_total = die_1 + die_2
        print("Dice total: " + str(dice_total))

        while True:
            reply = input("Would you like to roll again (y/n)? ")
            if reply == 'y' or reply == 'n':
                break
            else:
                print("Invalid entry, please enter y or n")
                continue

    print("Thank you for using my program.")
