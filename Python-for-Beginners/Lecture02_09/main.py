## Default Parameter of Function

def say_hello(user_name):
    print("hello", user_name)

say_hello("Nico")   # Success
say_hello()         # Error

## Set a default value for any argument in function
def say_hello01(user_name="Anonymous"):
    print("Hello", user_name)

say_hello01("Nico") # Success - Hello, Nico
say_hello01() # Success - Hello, Anonymous