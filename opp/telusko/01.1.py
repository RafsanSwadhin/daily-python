# constructor in inheritance
# method resolution order

### 1
'''
class A:

    def __init__(self):
        print("In A init")
    def feature_1(self):
        print("Feature 1 is working")
    def feature_2(self):
        print("Feature 2 is working")
    
class B(A):
    def feature_3(self):
        print("Feature 3 is working")
    
    def feature_4(self):
        print("Feature 4 is working")

s1 = B() #it will print In A init
s1 = A() #it will print In A init
'''
### 2
'''
class A:

    def __init__(self):
        print("In A init")
    def feature_1(self):
        print("Feature 1 is working")
    def feature_2(self):
        print("Feature 2 is working")
    
class B(A):
    def __init__(self):
        print("In B init")
    def feature_3(self):
        print("Feature 3 is working")
    
    def feature_4(self):
        print("Feature 4 is working")

s1 = B() #it will print In B init
'''
### 3

class A:

    def __init__(self):
        print("In A init")
    def feature_1(self):
        print("Feature 1 is working")
    def feature_2(self):
        print("Feature 2 is working")
    
class B(A):
    
    def __init__(self):
        super().__init__()
        print("In B init")
    def feature_3(self):
        print("Feature 3 is working")
    
    def feature_4(self):
        print("Feature 4 is working")

s1 = B() #it will print: In A init
        #                In B init