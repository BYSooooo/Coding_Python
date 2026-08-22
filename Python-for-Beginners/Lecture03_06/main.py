## Python Casino

from random import randint

print('Welcome to Python Casino!')

# Select random int from 1 to 50 
pc_choice = randint(1,50)

playing = True

while playing : 
    user_choice = int(input('Choose Number : '))
    if user_choice == pc_choice:
        print('You won!')
        playing = False
    elif user_choice > pc_choice:
        print("Lower!")
    elif user_choice < pc_choice:
        print("Higher!")