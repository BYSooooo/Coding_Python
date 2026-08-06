## 2-7. Multiple Parameter

# Function of Having Single Parameter
def say_hello1(user_name):
    print("Hello", user_name, "how are you?")

say_hello1("Nico")

# Function of Multiple Parameter
def say_hello2(user_name, user_age):
    print("Hello", user_name, "How are you?")

# Error Occured because having only 1 parameter.
say_hello2("Nico")
say_hello2("Nico", 12)

# Ordering Argument is important.
say_hello2(12, "Nico")

# Using of Multiple Parameter
def say_hello3(user_name, user_age):
    print("Hello", user_name, "How are you?")
    print("you are", user_age, "years old")

say_hello3("Nico", 12)