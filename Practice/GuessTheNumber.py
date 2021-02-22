# Welcome to guess the number!
import random

print(" Welcome to guess the number! ")
print("-" * 30)
print("Please choose a number between 0 and 10!")
user_input = int(input())

random_number = random.randint(0, 10)
difference = abs(random_number-user_input)

if user_input == random_number:
    print("Correct! You have guessed the number!")
else:
    print("You stink! You did not guess the number")
    print("The number was {}!".format(random_number))
    print("You were {} off!".format(difference))
