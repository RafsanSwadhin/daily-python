class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self,ot):
        m1 = self.m1 + ot.m1
        m2 = self.m2 + ot.m2
        m3 = Student(m1,m2)
        
        return  m3

s1 = Student(70,60)
s2 = Student(50,40)
m3 = s1 + s2

print(m3.m1)