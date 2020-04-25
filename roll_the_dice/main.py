from random import *


def roll_the_dice():
    print("This program is going to be like rolling two dice. It will show you two random numbers.")

    die_1 = randint(1, 6)
    print("Die One: " + str(die_1))

    die_2 = randint(1, 6)
    print("Die Two: " + str(die_2))

    dice_total = die_1 + die_2
    print("Dice total: " + str(dice_total))
