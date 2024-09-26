class Employee:
    def __init__(self):
        self.id = int(input("enter employee id"))
        self.name = input("enter employee name")
        self.salary = float(input("enter employee salary"))
        
    def display(self):
        print("employee id:",self.id)
        print("employee name:",self.name.title())
        print("employee salary:",self.salary)

a = Employee()
#a.putdata()
a.display()

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

