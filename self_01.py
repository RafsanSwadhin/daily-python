class Student:
    def set_details(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa 
    def display(self):
        print(f"Roll:{self.roll} & GPA:{self.gpa}")

s1 = Student()
s1.set_details(101,4.5)
s1.display()