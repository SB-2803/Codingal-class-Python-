from abc import ABC, abstractmethod
class SmartDevice(ABC):
    def show_device(self, name):
        print("Device Name:", name)
    @abstractmethod
    def turn_on(self):
        pass
class SmartPhone(SmartDevice):
    def turn_on(self):
        print("Smart Phone is now ON:)")
class SmartTV(SmartDevice):
    def turn_on(self):
        print("Smart TV is now ON:)")

phone = SmartPhone()
Television = SmartTV()
 
phone.show_device("Handheld Smartphone")
phone.turn_on()
 
Television.show_device("Bedroom TV")
Television.turn_on()
 
class SecurityCamera:
    def check_status(self):
        print("Security Camera is recording!!")
 
 
class SmartFan:
    def check_status(self):
        print("Smart fan is ON!!")
 
for device in (SmartFan(),SecurityCamera()):
    device.check_status()