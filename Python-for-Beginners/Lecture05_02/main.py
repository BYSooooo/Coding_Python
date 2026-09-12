## Classes

# Define Class
class Puppy:
    pass

ruffus = Puppy()
print(ruffus)

# Add Method Test
class Puppy1:
    def __init__():
        print("Puppy is born!")

ruffus1 = Puppy1()
# Puppy1 has Error because has no argument.
print(ruffus1)

# Add Method
class Puppy2:
    # All Method has one default argument
    # First argument of method is Reference of self
    def __init__(self):
        print(self)
        print("Puppy is born!")

ruffus2 = Puppy2()

# Define Argument
class Puppy3:
    def __init__(self):
        # Set a variable to argument
        self.name = "Ruffus"
        self.age = 0.1
        self.bread = "Beagle"

ruffus3 = Puppy3()

# check argument variable
print(ruffus3.name)
print(ruffus3.age)
print(ruffus3.bread)

