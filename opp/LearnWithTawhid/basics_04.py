class Student:
    def __init__(self,nm,id) :
        print("An Object is created")
        print("location of s1 object:",self)
        self.name = nm #local variable
        self.ID = id
        print(nm,id)
        print(self.name,self.ID)
s1 = Student("rafsan",454)
print("memory location of the object is:",s1)
print(s1.name)
print(s1.ID)
s2 = Student("rafsffffan",4545544)