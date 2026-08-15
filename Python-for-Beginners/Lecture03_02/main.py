## And Or

# input()
age = input("How old are you?")

print("user answer", age)

# type()
age2 = input("How old are you?")

print(type(age2))

# int()
age3 = int(input("How old are you?"))

if age3 < 18:
    print("You can't drink.")
else:
    print("Go ahead")

# and
age4 = int(input("How old are you?"))

if age4 < 18:
    print("You can't drink.")
elif age4 >= 18 and age4 <= 35:
    print("You drink beer!")
else:
    print("Go ahead")

#or
age5 = int(input("How old are you?"))

if age5 < 18:
    print("You can't drink.")
elif age5 >= 18 and age5 <= 35:
    print("You drink beer!")
elif age5 == 60 or age5 == 70:
    print("Birthday Party!")
else :
    print("Go ahead")