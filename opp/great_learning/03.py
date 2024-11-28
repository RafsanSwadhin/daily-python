## constructor

class Employee:
    def __init__(self,name,age,salary,gender):
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender
    
    def employee_details(self):
        print("Name of Employee is",self.name.title())
        print("Age of Employee is",self.age)
        print("Salarey of Employee is",self.salary)
        print("Gender of employee is",self.gender.title())

e1 = Employee("rafsan jani ahmed",22,200000,"male")
e1.employee_details()