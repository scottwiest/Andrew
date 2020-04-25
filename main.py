from mad_libs.main import *

welcome = "Welcome to Andrew's Repository. Please select which program you would like to run:\n"\
          "\t1 - Mad Libs\n"

print(welcome)

invalid_entry = "------------------------------------------------------------\n"\
                "\tInvalid Entry, please choose a number between 1 and 1\n"\
                "------------------------------------------------------------"
while True:
    try:
        selection = int(input("Please make a selection: "))
    except ValueError:
        print(invalid_entry)
        continue
    if selection != 1:
        print(invalid_entry)
        continue
    else:
        break

if selection == 1:
    mad_libs()
