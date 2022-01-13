#!/usr/bin/env python3

from scenes import *


def main():
    inventory = []

    scene1()
    while True:
        print_menu()
        answer = input("\nPlease select your choice 1-6"
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
            print("\nCongratulations!!! you made it out of the room")
            break

    print("GAME OVER")


if __name__ == "__main__":
    main()

