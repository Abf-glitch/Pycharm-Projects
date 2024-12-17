class Device:
    def __init__(self, model, yom):
        self.model = model
        self.yom = yom

    def crush(self):
        print(self.model, "has crashed")


computer = Device("HP", "2008")
computer.crush()

laptop = Device("Dell", "2008")
laptop.crush()
