## Inheritance Part 2

# Base Structure
class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

class Puppy(Dog):
    def woof_woof(self):
        print("Woof Woof")

class GuardDog(Dog):
    def rrrr(self):
        print("Stay away!")

ruffus = Puppy(
    name="Ruffus",
    breed="Beagle"
)

bibi = GuardDog(
    name="Bibi",
    breed="Dalmatian"
)
