### 1
class A:

    def __init__(self):
        print("In A init")
    def feature_1(self):
        print("Feature 1 is working")
    def feature_2(self):
        print("Feature 2 is working")
    
class B():
    
    def __init__(self):

        print("In B init")
    def feature_3(self):
        print("Feature 3 is working")
    
    def feature_4(self):
        print("Feature 4 is working")

class C(A,B):

    def __init__(self):
        print("In C init")




s1 = C() # it will print "In C init"

### 2
print()
class A:

    def __init__(self):
        print("In A init")
    def feature_1(self):
        print("Feature 1 is working")
    def feature_2(self):
        print("Feature 2 is working")
    
class B():
    
    def __init__(self):

        print("In B init")
    def feature_3(self):
        print("Feature 3 is working")
    
    def feature_4(self):
        print("Feature 4 is working")

class C(A,B):

    def __init__(self):
        super().__init__()
        print("In C init")

s1 = C() # it will print: "In A init" and "IN C init "

### 3
print()
print("MRO= method revolution ")
class A:

    def __init__(self):
        print("In A init")
    def feature_1(self):
        print("Feature 1 is working")
    def feature_2(self):
        print("Feature 2 is working")
    
class B():
    
    def __init__(self):

        print("In B init")
    def feature_3(self):
        print("Feature 3 is working")
    
    def feature_4(self):
        print("Feature 4 is working")

class C(A,B):

    def __init__(self):
        super().__init__()
        
        print("In C init") 
    
    def feat(self):
        super().feature_2()

s1 = C()
s1.feature_1()
s1.feat()

print()
class A:

    def __init__(self):
        print("In A init")
    def feature_1(self):
        print("Feature 1 is working")
    def feature_2(self):
        print("Feature 2 is working")
    
class B():
    
    def __init__(self):

        print("In B init")
    def feature_3(self):
        print("Feature 3 is working")
    
    def feature_4(self):
        print("Feature 4 is working")

class C(A,B):

    def __init__(self):
        super().__init__()
        print("In C init")

s1 = C() # it will print: "In A init" and "IN C init "

### 3
print()
print("take advantage from class B ")
class A:

    def __init__(self):
        print("In A init")
    def feature_1(self):
        print("Feature 1 is working")
    def feature_2(self):
        print("Feature 2 is working")
    
class B():
    
    def __init__(self):

        print("In B init")
    def feature_3(self):
        print("Feature 3 is working")
    
    def feature_4(self):
        print("Feature 4 is working")

class C(A,B):

    def __init__(self):
        super().__init__()
        B.__init__(self)
        print("In C init") 
    

s1 = C()
s1.feature_1()