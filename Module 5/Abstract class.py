#import necessary modules
from abc import ABC, abstractmethod
#create base class
class ABCclass(ABC):
    #function to print a value
    def print(self,x):
        print("Passed value:",x)
    #Abstract method
    @abstractmethod
    def task(self):
        print("we are inside the Abstract class:)")

#Create sub class
class test_class(ABCclass):
    def task(self):
        print("We are inside the test_class task!!!")

#object of test class created
test_obj = test_class()
test_obj.task()
test_obj.print(100)