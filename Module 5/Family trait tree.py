#Create the parent class with shared family traits
class Familymember:
    def __init__(self,eye_colour,height_cm):
        self.eye_colour = eye_colour
        self.height_cm = height_cm

    def show_traits(self):
        print("Eye colour:",self.eye_colour)
        print("Heght in cm:",self.height_cm)

#Create the child class that inherits from family member
class Kid(Familymember):
    def __init__(self,name,age,eye_colour,height_cm):
        self.name = name
        self.age = age
        super().__init__(eye_colour,height_cm)

    def show_traits(self):
        print("Name:",self.name)
        print("Age:",self.age)
        super().show_traits()

    def favouritehobby(self,hobby):
        print(self.name,"loves", hobby)

child = Kid("Maya",10,"Brown",140)
child.show_traits()
child.favouritehobby("painting")
print("Is Kid a subclass of familymember?",issubclass(Kid,Familymember))