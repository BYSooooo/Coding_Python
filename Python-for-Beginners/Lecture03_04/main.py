## Python Standard Library

# Basic
user_choice = int(input("Choose number."))
pc_choice = 50

if user_choice == pc_choice:
    print("You won!")
elif user_choice > pc_choice:
    print("Lower")
elif user_choice < pc_choice:
    print("Higher")

# Setting pc_choice Randomly
from random import randint

user_choice2 = int(input("Choose number."))
pc_choice2 = randint(5,10)

if user_choice2 == pc_choice2:
    print("You won!")
elif user_choice2 > pc_choice2:
    print("Lower. pc choice is ",pc_choice2)
elif user_choice2 < pc_choice2:
    print("Higher. pc choice is ",pc_choice2)