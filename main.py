from mad_libs.main import *
from roll_the_dice.main import *
from guess_the_number.main import *
from text_adventure.main import *

welcome = "Welcome to Andrew's Repository. Please select which program you would like to run:\n" \
          "\t1 - Mad Libs\n" \
          "\t2 - Roll the Dice\n" \
          "\t3 - Guess the Number\n" \
          "\t4 - Text Adventure"

print(welcome)

invalid_entry = "------------------------------------------------------------\n" \
                "\tInvalid Entry, please choose a number between 1 and 4\n" \
                "------------------------------------------------------------"
while True:
    try:
        selection = int(input("Please make a selection: "))
    except ValueError:
        print(invalid_entry)
        continue
    if selection <= 0 or selection > 4:
        print(invalid_entry)
        continue
    else:
        break

function_switch = {
    1: mad_libs,
    2: roll_the_dice,
    3: guess_the_number,
    4: text_adventure
}
function = function_switch.get(selection)
function()
