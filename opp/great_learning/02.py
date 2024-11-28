class Phone:
    def set_color(self,color):
        self.color = color
    def set_cost(self,cost):
        self.cost = cost
    def show_color(self):
        return self.color
    def show_cost(self):
        return self.cost
    def make_call(self):
        print("I am making a call")
    def play_game(self):
        print("I am playing a game")

p1 = Phone()
p1.set_color("green")
p1.set_cost(5000)

print(p1.set_color("green")) #---none
print(p1.set_cost(5000))  #---none

print(p1.show_color())
print(p1.show_cost())