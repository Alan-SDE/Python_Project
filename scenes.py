#!/usr/bin/env python3


def print_menu():
    print("\n1. Examine desk"
          "\n2. Examine bookshelf"
          "\n3. Examine coat rack"
          "\n4. Examine door"
          "\n5. Examine keypad"
          "\n6. Examine light switch")


def scene1():
    print("You awake to find yourself in a strange room."
          "\nThere are no windows and only one door with a keypad beside it."
          "\nThere is a bookshelf, a desk, a light switch, and a coat rack with a single coat in the room with you."
          "\nWhat would you like to do?")
    print_menu()


def examine_desk(inv):
    inventory = inv
    if 'key' in inventory:
        print("The key that you have looks like it would fit in this keyhole."
              "\nWould you like to try it (y/n)?\n")
        answer = input(">>")
        if answer.lower() == "y":
            print("The key works!"
                  "\nInside the unlocked desk you find a blacklight that has been added to your inventory")
            inventory.append('blacklight')

