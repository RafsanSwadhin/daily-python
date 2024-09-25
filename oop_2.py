class Calculator:

    def addition(self,a,b):
        return a+b
    def substraction(self,a,b):
        return a-b
    def multiplication(self,a,b):
        return a*b
    def division(seslf,a,b):
        try:
            return a/b
        except ZeroDivisionError:
            return 'It is impossilble to divide by zero'
        
my_calculator = Calculator()
cal = my_calculator.addition(54,53)
print(cal)

cal = my_calculator.division(54,0)
print(cal)