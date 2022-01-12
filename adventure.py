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


if __name__ == "__main__":
    main()

