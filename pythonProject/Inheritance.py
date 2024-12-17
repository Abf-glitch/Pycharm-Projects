# parent class/base class/Super class
class Animal:
    hasScales = True

    def sound(self):
        print("Animal is speaking")

# Child class/Sub class/Derived class
class Duck:
    hasWing = True

    def move(self):
        print("Duck is swimming")


class Mouse:
    def move(self):
        print("Mouse is walking")


a = Animal()

d = Duck()
print(d.hasWing)


m = Mouse()
