#create class
class IOString:
    #counstructor to set default value
    def __init__(self):
        self.str1 = ""
    #function to get input from user 
    def get_String(self):
        self.str1 = input("Enter a string: ")
    #function to print the string in upper case
    def print_string(self):
        if self.str1 == self.str1.upper():
             print("The result is:",self.str1.lower())
        else:
             print("The result is:",self.str1.upper())
#Object creation
str_obj = IOString()
#Call functions
str_obj.get_String()
str_obj.print_string()