### duck typing
print("step--1")
class Pycharm:

    def execute(self):
        print("Compiling")
        print("Running")

class Laptop:

    def code(self,ide):
        ide.execute()

ide = Pycharm()
l1 = Laptop()
l1.code(ide)

print()
print("step--2")
class Pycharm:

    def execute(self):
        print("Compiling")
        print("Running")

class My_ide:
    def execute(self):
        print("spell check")
        print("Convention check")


class Laptop:

    def code(self,ide):
        ide.execute()

#ide = Pycharm()
ide = My_ide()
l1 = Laptop()
l1.code(ide)

