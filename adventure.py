#!/usr/bin/env python3

from scenes import *


def main():
    inventory = ['key']

    scene1()
    while True:
        print_menu()
        answer = input("\nPlease select your choice 1-6"
                       "\n>>")
        if answer == '1':
            examine_desk(inventory)


if __name__ == "__main__":
    main()

