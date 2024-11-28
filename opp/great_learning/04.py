class Vehicle:
    def __init__(self,mileage,cost):
        self.mieage = mileage
        self.cost = cost

    def show_vehicle_details(self):
        print("Mileage of vehicle is ",self.mileage)
        print("Cost of vehicle is ",self.cost)
        print("I am a vehicle")
        