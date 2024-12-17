# Class is a blueprint of an object.
# Object is an instance of a class.

class Person:
    # Properties/attributes/Variables/Characteristics
    name = "James"
    age = 45
    gender = "Male"

    # Methods/Function/Behaviour

    def move(self):
        print(self.name, "is walking")


farmer = Person()
farmer.move()
print(farmer.gender)
