## Else && Elif

password_correct = True

# Case 1.
if password_correct:
    print("Here is your money") ## Called
else:
    print("Wrong Password.")

# Case 2.
password_correct2 = False

if password_correct2:
    print("Here is your money") 
else:
    print("Wrong Password.") ## Called

# Case 3.
winner = 10

if winner > 10:
    print("Winner is greater than 10")
elif winner < 10 : 
    print("Winner is less than 10")
else:
    print("Winner is 10") ## Called