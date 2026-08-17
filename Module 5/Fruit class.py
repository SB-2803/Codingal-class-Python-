class fruit:
    #class variable
    taste = "sweet"
    def __init__(self,name,colour):
        self.name = name
        self.colour = colour

mango = fruit("Mango","yellow")
strawberry = fruit("Strwaberry","Red")
print(mango.name,":")
print(mango.colour)
print(mango.taste)
print(strawberry.name,":")
print(strawberry.colour)
print(strawberry.taste)