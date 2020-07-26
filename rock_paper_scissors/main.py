from random import *


invalid_entry = "---------------------------------------------------------------------\n" \
                "\tInvalid entry. Please choose a number between 1 and 3\n" \
                "---------------------------------------------------------------------\n"


def rock_paper_scissors():
    continue_game = True
    while continue_game:
        while True:
            try:
                print("Let's play Rock, Paper, Scissors")
                print("\t1 - Rock\n"
                      "\t2 - Paper\n"
                      "\t3 - Scissors")
                user_rps = int(input("What do you choose? "))
            except ValueError:
                print(invalid_entry)
                continue
            if user_rps < 1 or user_rps > 3:
                print(invalid_entry)
                continue
            break

        if user_rps == 1:
            print("You chose Rock")
        elif user_rps == 2:
            print("You chose Paper")
        else:
            print("You chose Scissors")
        computer_rps = randint(1, 3)
        if computer_rps == 1:
            print("Computer chose Rock")
        elif computer_rps == 2:
            print("Computer chose Paper")
        else:
            print("Computer chose Scissors")

        if computer_rps == 1 and user_rps == 3 or \
                computer_rps == 2 and user_rps == 1 or \
                computer_rps == 3 and user_rps == 2:
            print("Computer Wins!")
        elif computer_rps == 1 and user_rps == 2 or \
                computer_rps == 2 and user_rps == 3 or \
                computer_rps == 3 and user_rps == 1:
            print("You Win!")
        else:
            print("It's a tie!")

        while True:
            reply = input("Would you like to play again (y/n)? ")
            if reply == 'y' or reply == 'n':
                continue_game = True if reply == 'y' else False
                break
            else:
                print("Invalid entry, please enter y or n")
                continue
