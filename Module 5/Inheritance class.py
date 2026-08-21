class Person(object):
    def __init__(self,name,number):
        self.name = name
        self.number = number
    def display(self):
        print(self.name)
        print(self.number)

class Employee(Person):
    def __init__(self,name,number,salary,post):
        self.salary = salary
        self.post = post
        Person.__init__(self,name,number)
    def display(self):
        print(self.salary)
        print(self.post)
        Person.display(self)
        
a = Employee("Rahul",886012,98769,"Intern")
a.display()