from mad_libs.main import *
from roll_the_dice.main import *

welcome = "Welcome to Andrew's Repository. Please select which program you would like to run:\n"\
          "\t1 - Mad Libs\n"\
          "\t2 - Roll the Dice\n"

print(welcome)

invalid_entry = "------------------------------------------------------------\n"\
                "\tInvalid Entry, please choose a number between 1 and 2\n"\
                "------------------------------------------------------------"
while True:
    try:
        selection = int(input("Please make a selection: "))
    except ValueError:
        print(invalid_entry)
        continue
    if selection < 0 or selection > 2:
        print(invalid_entry)
        continue
    else:
        break

if selection == 1:
    mad_libs()

if selection == 2:
  roll_the_dice()