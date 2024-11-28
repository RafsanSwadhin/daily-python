class Student:
    #paramaterized constructor    
    def __init__(self,name,roll):
        self.name = name.title() #instance variable
        self.id = roll  #instance variable
        print("a student object has been created")
    

s1 = Student("rafsan",55)

print(s1.id)
s1.id = 44
print(s1.id)
print(s1.name)