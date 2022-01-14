#!/usr/bin/env python3
import os


# used to clear the console between scenes
def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


# prints menu
def print_menu():
    clear_console()
    print("\nWhat would you like to do?"
          "\n1. Examine desk"
          "\n2. Examine bookshelf"
          "\n3. Examine coat rack"
          "\n4. Examine keypad"
          "\n5. Examine light switch"
          "\ni. view inventory"
          "\nq. quit")


# opening scene displays ascii intro and describes the room.
def scene1():
    clear_console()
    with open('images/intro.txt', 'r') as f:
        for line in f:
            print(line.rstrip())
    print("\nYou awake to find yourself in a strange room."
          "\nThere are no windows and only one door with a keypad beside it."
          "\nThere is a bookshelf, a desk, a light switch, and a coat rack with a single coat in the room with "
          "you."
          "\nSearch for clues and items to help you open the door and escape.")
    input("\nPress enter to continue")


# desk scene prints ascii desk and appropriate text based on inventory.
def examine_desk(inv):
    clear_console()
    with open('images/desk.txt', 'r') as f:
        for line in f:
            print(line.rstrip())
    inventory = inv
    if 'blacklight' in inventory:  # checks to see if you already have the blacklight in your inventory.
        print("You've already found what was hidden in the desk.")
        input("\nPress enter to continue")
        return inventory
    elif 'key' in inventory:  # Checks to see if you have the key in your inventory.
        print("\nYou see a desk with a locked drawer and a key hole."
              "\nThe key that you have looks like it would fit in this keyhole."
              "\nWould you like to try it (y/n)?\n")
        answer = input(">>")
        # provides output based on players answer
        if answer.lower() == "y":
            print("The key works!"
                  "\nInside the unlocked desk you find a blacklight.\n"
                  "\nBlacklight has been added to your inventory.")
            inventory.append('blacklight')  # adds blacklight to your inventory
            input("\nPress enter to continue")
            return inventory
        elif answer.lower() == "n":
            return inventory
        else:
            print("Invalid response: Please select y or n!")
    else:
        print("\nYou see a desk with a locked drawer and a key hole. You probably need to find a key.")
        input("\nPress enter to continue")
        return inventory


#  bookshelf scene prints ascii bookshelf and asks for password, if password is correct, prints ascii bookshelf answer.
def examine_bookshelf():
    clear_console()
    with open('images/bookshelf.txt', 'r') as f:
        for line in f:
            print(line.rstrip())
    print("\nThere are 5 rows of books but none of them will move."
          "\nOn the top shelf, you notice a five letter dial lock."
          "\nWould you like to try to guess the password? y/n")
    answer = input(">>")
    if answer.lower() == 'y':
        while True:  # loops until correct answer is given or player quits
            password = input("\nPlease enter your guess or q to give up."
                             "\n>>")
            if password.lower() == "death":
                clear_console()
                with open('images/book_answer.txt', 'r') as f:
                    for line in f:
                        print(line.rstrip())
                print("\nYou hear a click and the top row of books lifts up to reveal the following message:\n"
                      "\nI.B.N.F.E local 8251")
                break
            elif password.lower() == "q":
                print("\nNobody likes a quitter, but ok.")
                break
            else:
                print("Incorrect password: Please try again")
    input("\nPress enter to continue")


# coat rack scene prints ascii coat and checks if key is in inventory. if not, adds key to inventory
def examine_coatrack(inv):
    clear_console()
    with open('images/coat.txt', 'r') as f:
        for line in f:
            print(line.rstrip())
    inventory = inv
    if 'key' not in inventory:
        print("\nYou search through the coat and find a key hidden in one of the pockets."
              "\nI wonder what this key could be used for?\n"
              "\nkey has been added to your inventory.")
        inventory.append('key')  # adds key to inventory
        input("\nPress enter to continue")
        return inventory
    else:
        print("You don't see anything else in the jacket or on the coat rack.")
        input("\nPress enter to continue")
        return inventory


# keypad scene prints ascii keypad and prompts for password.  If correct password is given, adds open to inventory.
def examine_keypad(inv):
    clear_console()
    with open('images/keypad.txt', 'r') as f:
        for line in f:
            print(line.rstrip())
    inventory = inv
    print("\nYou see a numerical keypad with the numbers 0-9."
          "\nWould you like to try to guess the password? y/n")
    answer = input(">>")
    if answer.lower() == 'y':
        while True:  # loops until correct answer is given or player quits
            password = input("\nPlease enter your guess or q to give up."
                             "\n>>")
            if password == "8251":
                print("\nYou hear a gears turning and the door slowly opens.\n")
                inventory.append('open')
                break
            elif password.lower() == "q":
                print("\nNobody likes a quitter, but ok.")
                break
            else:
                print("Incorrect password: Please try again.")
        input("\nPress enter to continue")
        return inventory
    else:
        return inventory


# lightswitch scene prints ascii light switch and checks inventory for blacklight, then provides appropriate response
def examine_lightswitch(inv):
    clear_console()
    with open('images/light.txt', 'r') as f:
        for line in f:
            print(line.rstrip())
    if 'blacklight' in inv:
        print("\nGreat! Now you can't see."
              "\nWould you like to use the blacklight? y/n")
        answer = input("\n>>")
        if answer.lower() == 'y':
            clear_console()
            with open('images/blacklight.txt', 'r') as f:
                for line in f:
                    print(line.rstrip())
            print("\nAs you turn on the blacklight, you see some writing on the wall with an arrow pointing to the "
                  "bookshelf."
                  '\nThe writing says "The debt that all men pay."')
        elif answer.lower() == 'n':
            print('Ok, better turn that light back on.')
        else:
            print("Invalid response: Please enter y or n.")
    else:
        print("\nGreat! Now you can't see."
              "\nBetter turn that light back on.")
    input("\nPress enter to continue")


# prints items in the players inventory
def view_inventory(inv):
    clear_console()
    if len(inv) == 0:
        print("\nThere is nothing in your inventory yet. Keep looking around.")
        input("\nPress enter to continue.")
    else:
        print("\nYour inventory contains:")
        for item in inv:
            print(item)
        input("\nPress enter to continue.")
