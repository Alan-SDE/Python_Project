#!/usr/bin/env python3
""" Simple escape room game for console.
    The object is to search the room to find hidden objects and clues to solve the problems and escape."""

from scenes import *


def main():
    # creates a list to use as your inventory
    inventory = []
    # Starts scene one
    scene1()
    while True:  # loops until game is over or player quits
        print_menu()
        answer = input("\nPlease select your choice 1-5, i, or q"
                       "\n>>")
        if answer == '1':
            inventory = examine_desk(inventory)
        elif answer == '2':
            examine_bookshelf()
        elif answer == '3':
            inventory = examine_coatrack(inventory)
        elif answer == '4':
            inventory = examine_keypad(inventory)
        elif answer == '5':
            examine_lightswitch(inventory)
        elif answer.lower() == 'i':
            view_inventory(inventory)
        elif answer.lower() == 'q':
            break
        else:
            print("Invalid selection: Please enter 1-5, i, or q.")

        if 'open' in inventory:
            clear_console()
            with open('images/escaped.txt', 'r') as f:
                for line in f:
                    print(line.rstrip())
            print("\nCongratulations!!! you made it out of the room\n")
            break

    print("\nGAME OVER\n")


if __name__ == "__main__":
    main()
