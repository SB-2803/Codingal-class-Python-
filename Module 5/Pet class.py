class pet:
    species = "Dog"
    def __init__(self,name,colour,breed,age):
        self.name = name
        self.colour = colour
        self.breed = breed
        self.age = age

Coco = pet("Coco","Brown","Labrador",5)
Alex = pet("Alex","White","Husky",6)
print("All about",Coco.name,":")
print("Age:",Coco.age)
print("Species:",Coco.species)
print("Breed:",Coco.breed)
print("Colour:",Coco.colour)

print("\nAll about",Alex.name,":")
print("Age:",Alex.age)
print("Species:",Alex.species)
print("Breed:",Alex.breed)
print("Colour:",Alex.colour)