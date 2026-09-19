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

# Error - no Argument about 'age'
ruffus = Puppy(
    name="Ruffus",
    breed="Beagle"
)

bibi = GuardDog(
    name="Bibi",
    breed="Dalmatian"
)

# Add Control of age Argument
class Puppy2(Dog):
    def __init__(self, name, breed):
        # super() = Reference of class Dog
        super().__init__(
            name,
            breed,
            0.1
        )

    def woof_woof(self):
        print("Woof Woof")

class GuardDog2(Dog):
    def __init__(self, name, breed):
        super().__init__(name, breed, 5)

    def rrrr(self):
        print("Stay away!")

# Don't need to add age argument because it is handled in each Class
ruffus2 = Puppy2(name="Ruffus", breed = "Beagle")
bibi2 = GuardDog2(name="Bibi", breed="Dalmatian")

print(ruffus2.age)  # 0.1
print(bibi2.age)    # 5