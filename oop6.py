class Faculty:
    def __init__(self,a,b,c):
        self.id = a
        self.name = b
        self.salary = c
        
    def display(self):
        print("faculty id:",self.id)
        print("faculty name:",self.name.title())
        print("faculty salary:",self.salary)

b = Faculty(1,"rafsan jani",656565656565656565)
#a.putdata()
b.display()