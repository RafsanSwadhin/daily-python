class House:
    def __init__(self) :
        self.window = 4
        self.door = 2
    def view(self):
        print(self.window , "windows", self.door , "doors")
h1 = House()
h1.view()
h1.door = 455
h1.view()