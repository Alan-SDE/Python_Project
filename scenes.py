#!/usr/bin/env python3


def print_menu():
    print("\nWhat would you like to do?"
          "\n1. Examine desk"
          "\n2. Examine bookshelf"
          "\n3. Examine coat rack"
          "\n4. Examine keypad"
          "\n5. Examine light switch"
          "\ni. view inventory"
          "\nq. quit")


def scene1():
    print("You awake to find yourself in a strange room."
          "\nThere are no windows and only one door with a keypad beside it."
          "\nThere is a bookshelf, a desk, a light switch, and a coat rack with a single coat in the room with you.\n")
    input("\nPress enter to continue")

def examine_desk(inv):
    inventory = inv
    if 'blacklight' in inventory:
        print("You've already found what was hidden in the desk.")
        return inventory
    elif 'key' in inventory:
        print("\nYou see a desk with a locked drawer and a key hole."
              "\nThe key that you have looks like it would fit in this keyhole."
              "\nWould you like to try it (y/n)?\n")
        answer = input(">>")
        if answer.lower() == "y":
            print("The key works!"
                  "\nInside the unlocked desk you find a blacklight.\n"
                  "\nBlacklight has been added to your inventory.")
            inventory.append('blacklight')
            return inventory
        elif answer.lower() == "n":
            return inventory
        else:
            print("Invalid response: Please select y or n!")
    else:
        print("\nYou see a desk with a locked drawer and a key hole. You probably need to find a key.")
        return inventory
    input("\nPress enter to continue")


def examine_bookshelf():
    print("\nThere are 5 rows of books but none of them will move."
          "\nOn the top shelf, you notice a five letter dial lock."
          "\nWould you like to try to guess the password? y/n")
    answer = input(">>")
    if answer.lower() == 'y':
        while True:
            password = input("\nPlease enter your guess or q to give up."
                             "\n>>")
            if password.lower() == "death":
                print("\nYou hear a click and the top row of books lifts up to reveal the following message:\n"
                      "\nI.B.N.F.E local 8251")
                break
            elif password.lower() == "q":
                print("\nNobody likes a quitter, but ok.")
                break
            else:
                print("Incorrect password: Please try again")
    input("\nPress enter to continue")


def examine_coatrack(inv):
    inventory = inv
    if 'key' not in inventory:
        print("\nYou search through the coat and find a key hidden in one of the pockets."
              "\nI wonder what this key could be used for?\n"
              "\nkey has been added to your inventory.")
        inventory.append('key')
        return inventory
    else:
        print("You don't see anything else in the jacket or on the coat rack.")
        return inventory
    input("\nPress enter to continue")


def examine_keypad(inv):
    inventory = inv
    print("\nYou see a numerical keypad with the numbers 0-9."
          "\nWould you like to try to guess the password? y/n")
    answer = input(">>")
    if answer.lower() == 'y':
        while True:
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
        return inventory
    else:
        return inventory
    input("\nPress enter to continue")


def examine_lightswitch(inv):
    if 'blacklight' in inv:
        print("\nGreat! Now you can't see."
              "\nWould you like to use the blacklight? y/n")
        answer = input("\n>>")
        if answer.lower() == 'y':
            print("\nAs you turn on the blacklight, you see some writing on the wall with an arrow pointing to the "
                  "bookshelf."
                  '\nThe writting says "The debt that all men pay."')
        elif answer.lower() == 'n':
            print('Ok, better turn that light back on.')
        else:
            print("Invalid response: Please enter y or n.")
    else:
        print("\nGreat! Now you can't see."
              "\nBetter turn that light back on.")
    input("\nPress enter to continue")