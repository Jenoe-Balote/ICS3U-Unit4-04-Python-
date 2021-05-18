#!/usr/bin/env python3

# Created by Jenoe Balote
# Created on May 2021
# This program is the better "Number Guessing Game"

import random
import string
import constants
random_number = random.randint(0, 10)


def main():
    # this function runs the better "Number Guessing Game"

    # input process and output
    while True:
        number_guess = str(input("Enter a number between 0 - 10: "))
        try:
            number_guess = int(number_guess)
            if number_guess >= constants.MIN and number_guess <= constants.MAX:
                if number_guess == random_number:
                    print("You guessed correctly!")
                    break
                elif number_guess > random_number:
                    print("Too high!")
                elif number_guess < random_number:
                    print("Too low!")
                else:
                    print("Invalid.")
            else:
                print("Invalid.")
                break
        except Exception:
            print("That is not a number at all!")
            break
    print("")
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
