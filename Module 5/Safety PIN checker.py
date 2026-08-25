class Passcode:
    def __init__(self,pwd=0):
        self.pwd = pwd
    def __str__(self):
        return("{0} is the current password".format(self.pwd))
    
password = int(input("Enter any password:"))
psc = Passcode(password)
print(psc)

class Safe:
    
    __PIN = 1234
    def __private(self):
        print("This is a very private safe. I WILL NOT TELL YOU MY PIN!!!")
    def print(self):
        print("My pin is:",Safe.__PIN)

Pin = Safe()
Pin.print()
Pin.__private()