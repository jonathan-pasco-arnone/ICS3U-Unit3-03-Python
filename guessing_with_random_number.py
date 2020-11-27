#!/usr/bin/env python3

# Created by: Jonathan Pasco-Arnone
# Created on: November 2020
# This program determines if the user guesses
# a randomly generated number correctly

import math
import random


def main():
    # This function obtains an input from the user and the computer and
    # determines if the user's guess is correct

    print("This program makes the user guess the number that"
          "the computer has saved.")
    print("")
    randomly_generated_number = random.randint(0, 9)
    guess = int(input("Please input a number (from 0 to 9): "))
    if guess == randomly_generated_number:
        print("You guessed correctly!")
    else:
        print("Incorrect try again")


if __name__ == "__main__":
    main()
