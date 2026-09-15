## Methods

# Base Structure
class Puppy:
    def __init__(self):
        self.name = "Ruffus"
        self.age = 0.1
        self.breed = "Beagle"

bibi = Puppy()
ruffus = Puppy()

print(bibi.name, ruffus.name) # "Ruffus, Ruffus"

# Add to Customize
class Puppy2:
    def __init__(self, name, breed):
        self.name = name
        self.age = 0.1
        self.breed = breed

ruffus = Puppy2("Ruffus", "Beegle")
bibi = Puppy2("Bibi", "Dalmatian")

print(ruffus.name, bibi.name)

# Change Argument structure
ruffus2 = Puppy2(
    name = "Ruffus", 
    breed = "Beegle"
)

bibi2 = Puppy2(
    name="Bibi", 
    breed="Dalmatian"
)

print(ruffus.name, bibi.name)

# Test __str__
class Puppy3:
    def __init__(self, name, breed):
        self.name = name
        self.age = 0.1
        self.breed = breed
    ## return value of '__str__' is connected to print() function
    ## Must return string
    def __str__(self):
        return f"{self.breed} puppy named {self.name}"

ruffus3 = Puppy3(name="Ruffus",breed="Beagle")
bibi3 = Puppy3(name="Bibi", breed="Dalmatian")

print(ruffus3,bibi3)
