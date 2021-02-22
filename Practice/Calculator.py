# The NEW calculator program.
# Made by Kendrick Taylor.
print(" Welcome to the calculator program! ")
print("-" * 39)
choice = input("Choose 1 to add, 2 to subtract, 3 to multiply, and 4 to divide -> ")
if choice == "1" or choice == "2" or choice == "3" or choice == "4":
    num_1 = int(input("Enter first number -> "))
    num_2 = int(input("Enter second number -> "))
    if choice == "1":
        print(f"{num_1} added by {num_2} is: {num_1 + num_2}")
        print(" Thank you for using the calculator program! ")
        print("-" * 45)
    if choice == "2":
        print(f"{num_1} subtracted by {num_2} is: {num_1 - num_2}")
        print(" Thank you for using the calculator program! ")
        print("-" * 45)
    if choice == "3":
        print(f"{num_1} multiplied by {num_2} is: {num_1 * num_2}")
        print(" Thank you for using the calculator program! ")
        print("-" * 45)
    if choice == "4":
        print(f"{num_1} divided by {num_2} is: {num_1 / num_2}")
        print(" Thank you for using the calculator program! ")
        print("-" * 45)
else:
    print("You've made an invalid selection.")
    print("Next time, would you please use this calculator to do something useful.")
    print("\n Thank you for using the calculator program anyways! ")
    print("-" * 53)
# End of Calculator program.
# By Kendrick Taylor
