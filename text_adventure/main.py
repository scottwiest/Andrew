from time import sleep

directions = ["North", "East", "South", "West"]
name_str = "Name"
description_str = "Description"

rooms = {"lobby": {
        name_str: "Lobby",
        description_str: "You see a mummy's tomb creaking open",
        directions[0]: "dining_room",
        directions[1]: "garage",
        directions[2]: "bathroom",
        directions[3]: "reading_room"
    },
    "dining_room": {
        name_str: "Dining room",
        description_str: "You see food disappearing in teeth marks.",
        directions[0]: "wall",
        directions[1]: "garden",
        directions[2]: "lobby",
        directions[3]: "kitchen"
    },
    "garage": {
        name_str: "Garage",
        description_str: "You see a car, starting by its self.",
        directions[0]: "garden",
        directions[1]: "way_out",
        directions[2]: "ghost_invaded",
        directions[3]: "lobby"
    },
    "bathroom": {
        name_str: "Bathroom",
        description_str: "You hear something saying \"Hello, handsome.\"",
        directions[0]: "lobby",
        directions[1]: "ghost_invaded",
        directions[2]: "wall",
        directions[3]: "guest_room"
    },
    "reading_room": {
        name_str: "Reading room",
        description_str: "You see a book floating on a chair.",
        directions[0]: "kitchen",
        directions[1]: "lobby",
        directions[2]: "guest_room",
        directions[3]: "wall"
    },
    "garden": {
        name_str: "Garden",
        description_str: "You see a rake, raking the leaves.",
        directions[0]: "wall",
        directions[1]: "wall",
        directions[2]: "garage",
        directions[3]: "dining_room"
    },
    "kitchen": {
        name_str: "Kitchen",
        description_str: "You see chef hats moving around.",
        directions[0]: "wall",
        directions[1]: "dining_room",
        directions[2]: "reading_room",
        directions[3]: "wall"
    },
    "guest_room": {
        name_str: "Guest room",
        description_str: "You hear snoring and see a lump on the bed.",
        directions[0]: "reading_room",
        directions[1]: "bathroom",
        directions[2]: "wall",
        directions[3]: "wall"
    }
}

invalid_entry = "---------------------------------------------------------------------\n" \
                "\tInvalid entry. Please choose a number between 1 and " + str(len(directions)) + "\n" \
                "---------------------------------------------------------------------\n"


def text_adventure():
    print("Welcome to The Ghost House. You will navigate though by typing 1=North, 2=East, 3=South, and 4=West.\n"
          "There is one exit so navigate well. You will start in the Lobby.")
    curr_room = "lobby"
    while curr_room != "way_out":
        while True:
            try:
                print("------------------------------------------------------------------------")
                print("Now you are in " + rooms[curr_room][name_str] + ". " + rooms[curr_room][description_str])
                print("------------------------------------------------------------------------")
                print("Directions you can go:")
                for idx, direction in enumerate(directions):
                    idx_1 = idx + 1
                    print(str(idx_1) + " - " + direction)
                direction_number = int(input("Where do you want to go? "))
            except ValueError:
                print(invalid_entry)
                continue
            if direction_number < 1 or direction_number > len(directions):
                print(invalid_entry)
                continue
            break
        peak_room = rooms[curr_room][directions[direction_number - 1]]
        print("You move to the " + directions[direction_number - 1])
        sleep(1)
        print(". . .")
        sleep(1)
        if peak_room == "wall":
            print("-------------------------------------------------")
            print("You have hit a wall, you can't go that direction!")
            print("-------------------------------------------------")
        elif peak_room == "ghost_invaded":
            print("-------------------------------------------------")
            print("Ghosts are attacking you. You return to the lobby.")
            print("-------------------------------------------------")
            curr_room = "lobby"
        else:
            curr_room = peak_room

    print("----------------------------------------------------")
    print("Congratulations! You made it out of the Ghost House!")
    print("----------------------------------------------------\n")
    print("Thank you for using my program.")
