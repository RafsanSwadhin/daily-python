class Student:
    def __init__(self,nm,id) :
        print("An Object is created")
        name = nm #local variable
        ID = id
        print(name,ID)
s1 = Student("rafsan",22)


print("memory location of the object is:",s1)
