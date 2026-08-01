# Case 1
def say_hello():
    print("Hello how are you?")

def say_bye():
    print("bye bye")

say_hello()

## say_bye() => return "bye bye"

# Case 2
def say_hello2():
    print("Hello how are you?")

def say_bye2():
    print("bye bye")
    say_hello()

## say_bye() => return "bye bye" "Hello how are you?"