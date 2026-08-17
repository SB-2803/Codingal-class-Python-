#create a class
class parrot:
    #class attribute
    species = "bird"
    #instance attribute
    def __init__(self,name,age):
        self.name = name
        self.age = age

#instantiate the Parrot class
blu = parrot("Blu",10)
woo = parrot("Woo",15)

#access the class attribute
print("Blu is a {}".format(blu.species))
print("Woo is also a {}".format(woo.species))

#access the instance attribute
print(blu.name,"is",blu.age,"years old!!")
print(woo.name,"is",woo.age,"years old!!")