## Classes

# Declar of Class
class Puppy:
    pass

ruffus = Puppy()
print(ruffus)

# Add Method
class Puppy2:
    # All Method has one default argument
    # First argument of method is Reference of self
    def __init__(self):
        print(self)
        print("Puppy is born!")

ruffus2 = Puppy2()
