#create class
class Vehicle:
    #create init mthod
    def __init__(self, max_speed, mileage):
        #bind the arguements
        self.max_speed = max_speed
        self.mileage = mileage

#Object creation
modelX = Vehicle(240,18)
#access the variables inside the init method
print("Model max speed:",modelX.max_speed)
print("Model mileage:",modelX.mileage)