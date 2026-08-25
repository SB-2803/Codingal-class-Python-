#Class creation 
class Myclass:
    #private variable creation
    __private = 27
    #private method
    def __Private(self):
        print("I am inside class Myclass!!")
    #function to print value of private variable
    def hello(self):
        print("Private Variable Value:",Myclass.__private)

#Object creation and method call
foo = Myclass()
foo.hello()
foo.__Private