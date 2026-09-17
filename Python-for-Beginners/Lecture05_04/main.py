## Inheritance

# Base Structure
class Puppy:
    def __init__(self, name, breed):
        self.name = name
        self.age = 0.1
        self.breed = breed

    def __str__(self):
        return f"{self.breed} puppy named {self.name}"

# Add Custom Method
class Puppy2:
    def __init__(self, name, breed):
            self.name = name
            self.age = 0.1
            self.breed = breed
    
    def __str__(self):
        return f"{self.breed} puppy named {self.name}"

    # Add Custom Method.
    # Must have argument of self refrence of class
    def woof_woof(self):
        print("Woof Woof")

ruffus = Puppy2(name= "Ruffus", breed="Beagle")
ruffus.woof_woof()

# Add more method
class Puppy3:
    def __init__(self, name, breed):
        self.name = name
        self.age = 0.1
        self.breed = breed
         
    def __str__(self):
        return f"{self.breed} puppy named {self.name}"

    def woof_woof(self):
        print("Woof Woof")

    def introduce(self):
        self.woof_woof()
        print(f"My name is {self.name} and I am a baby {self.breed}")
        self.woof_woof()

ruffus = Puppy3(name="Ruffus", breed="Beagle")
ruffus.introduce()

# Interitance of Puppy
class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

class Puppy4(Dog):
    def woof_woof(self):
        print("Woof Woof")

    def introduce(self):
        self.woof_woof()
        print(f"My name is {self.name} and I am a baby {self.breed}")
        self.woof_woof()

class GuardDog(Dog):
    
    def rrrr(self):
        print("Stay away!")
        