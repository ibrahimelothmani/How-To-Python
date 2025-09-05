from OOP.human import Human


class Woman(Human):
    def __init__(self, name, age):
        super().__init__(name, age)

    def work(self):
        return f"{self.name} is working diligently!"
