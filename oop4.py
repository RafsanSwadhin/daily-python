class First:
    n = 63
obj = First()
print(obj.n)
class Employee:
    def putdata(self):
        self.id = int(input("enter employee id"))
        self.name = input("enter employee name")
        self.salary = float(input("enter employee salary"))
        
    def display(self):
        print("employee id:",self.id)
        print("employee name:",self.name.title())
        print("employee salary:",self.salary)

a = Employee()
a.putdata()
a.display()