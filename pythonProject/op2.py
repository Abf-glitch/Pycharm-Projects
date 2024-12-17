class Car:
    def __init__(self, model, color, manufacturer, yop):
        self.model = model
        self.color = color
        self.manufacturer = manufacturer
        self.yop = yop

    def speed(self):
        print("The manufacturer of ", self.model, " is ", self.manufacturer)


car1 = Car("B12", "White", "BMW", "2018")
car1.speed()

car2 = Car("c17", "Red", "Tesla", "2018")
car2.speed()

car3 = Car("GlE", "Black", "Mercedes", "2018")
car3.speed()
