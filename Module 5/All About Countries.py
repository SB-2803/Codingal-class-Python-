#Class 1 
class India():
    def capital(self):
        print("New Delhi is the capital of India.")
    def language(self):
        print("Hindi is the most widely spoken language in India.")
    def type(self):
        print("India is a developing country.")

#Class 2
class USA():
    def capital(self):
        print("Washington D.C. is the capital of India.")
    def language(self):
        print("English is the most widely spoken language in USA.")
    def type(self):
        print("USA is a developed country.")

#Object creation
obj_ind = India()
obj_usa = USA()

#common interface
for i in (obj_ind,obj_usa):
    i.capital()
    i.language()
    i.type()