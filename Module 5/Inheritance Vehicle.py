class Vehicle:
    def __init__(self, brand, colour):
        self.brand = brand
        self.colour = colour

    def show_details(self):
        print("Brand:", self.brand)
        print("Colour:", self.colour)

class Car(Vehicle):
    def __init__(self, model, seats, brand, colour):
        self.model = model
        self.seats = seats
        super().__init__(brand, colour)

    def show_details(self):
        print("Model:", self.model)
        print("Seats:", self.seats)
        super().show_details()

    def fuel_type(self, fuel):
        print(self.model, "uses", fuel)


obj = Car("Elevate", 5, "Honda", "Brown")
obj.show_details()
obj.fuel_type("Diesel")
print("Is Car a subclass of Vehicle?", issubclass(Car, Vehicle))
