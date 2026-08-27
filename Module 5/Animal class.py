#import necessary packages
from abc import ABC, abstractmethod
#create a base class
class Animal(ABC):
    #abstract method should be implemented by all sub-classes
    @abstractmethod
    def move(self):
        pass

#sub - classes
class Human(Animal):
    def move(self):
        print("I can walk and run.")
class Lion(Animal):
    def move(self):
        print("I can roar.")
class Snake(Animal):
    def move(self):
        print("I can crawl.")
class Dog(Animal):
    def move(self):
        print("I can bark.")

#Driver code(object)
R = Human()
R.move()
K = Lion()
K.move()
S = Snake()
S.move()
P = Dog()
P.move()