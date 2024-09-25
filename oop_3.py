class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b 

    def addition(self):
        return self.a+self.b
    def substraction(self):
        return self.a-self.b
    def multiplication(self):
        return self.a*self.b
    def division(self):
        try:
            return self.a/self.b
        except ZeroDivisionError:
            return 'It is impossilble to divide by zero'
    
my_cal = Calculator(45,7)
cal =     my_cal.addition()
print(cal)
