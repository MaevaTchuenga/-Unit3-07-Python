#!/usr/bin/env python3
# Created By: Maeva Tchuenga
# Date: 09, 12 2026
# this program is to generate a random age between 25 and 40
# and ask the user to enter a random age between 25 and 40 exclusive.
# The program will then check if the user's guess is correct and provide feedback accordingly.
# The program also handles invalid inputs and ensures that the user's guess is within the specified range
from multiprocessing import Value
import random


def main():

    # Generate any random_age between 25 and 40
    random_age = random.randint(25, 40)
    print(f"Random age generated: {random_age}")


user_input = int(input("Enter a user_age between 25 and 40: "))

# Check if the input is an integer
try:
    user_age_int = int(user_input)

    # Check if the user_input is within the range 25 to 40
    if user_input <= 25 or user_input >= 40:
        print("sorry!the user cannot date my grand daughter.")
    elif user_input < 25:
        print(" too young!user cannot date my grand daughter! Please pick a number from 25 to 40.")
    elif user_input > 40:
        print("too old! Please pick a number from 25 to 40.")
    else:
        print(f"perfect! welcome into the family {user_age_int}.")

except ValueError:
    print("sorry! the user_input is not an integer.")

if __name__ == "__main__":
    main()
