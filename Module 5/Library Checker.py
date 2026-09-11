class Matilda:
    def __init__(self,title,author,is_borrowed):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
    def borrow(self):
        self.is_borrowed = True
    def return_book(self):
        self.is_borrowed=False
    def display(self):
        print("Title:",self.title)
        print("Author:",self.author)
        if self.is_borrowed == False:
            print("The book is not borrowed. It has been returned:) \nIs_borrowed = False ")
        else:
            print("The book is borrowed. It has not been yet:( \nIs_borrowed = True")
class Famous_Five:
    def __init__(self,title,author,is_borrowed):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
    def borrow(self):
        self.is_borrowed = True
    def return_book(self):
        self.is_borrowed=False
    def display(self):
            print("Title:",self.title)
            print("Author:",self.author)
            if self.is_borrowed == False:
                print("The book is not borrowed. It has been returned:) \nIs_borrowed = False ")
            else:
                print("The book is borrowed. It has not been yet:( \nIs_borrowed = True")
class A_Study_In_Scarlet:
    def __init__(self,title,author,is_borrowed):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
    def borrow(self):
        self.is_borrowed = True
    def return_book(self):
        self.is_borrowed=False
    def display(self):
            print("Title:",self.title)
            print("Author:",self.author)
            if self.is_borrowed == False:
                print("The book is not borrowed. It has been returned:) \nIs_borrowed = False ")
            else:
                print("The book is borrowed. It has not been yet:( \nIs_borrowed = True")

asis = A_Study_In_Scarlet("A Study in Scarlet","Arthur Conan Doyle",False)
m = Matilda("Matilda","Ruskin Bond",True)
ff = Famous_Five("Famous Five","Enid Blyton",False)
asis.display()
m.display()
ff.display()