def say_hello_01():
    print('Hello. How are you?')

# This Function not ready for get a Data from outside.
say_hello_01("Nico") # => Error Occured.

def say_hello_02(user_name):
    print('Hello. How are you?')

# This Function ready for data from outside.
# but no use that data inside Function.
say_hello_02("Nico") # => Hello. How are you?

def say_hello_03(user_name):
    print("Hello,", user_name, "How are you?")

# This Function ready for data from outside.
# and use user_name in print()
say_hello_03("Nico") #=> Hello, Nico How are you?

# Function re-use making once.
say_hello_03("lynn") #=> Hello, lynn How are you?

## Summary
# In def Function - user_name = Parameter
def say_hello_04(user_name):
    print("Hello",user_name,"Hwo are you?") 

#In Function Call - "Nico" = Argument
say_hello_04("Nico")
