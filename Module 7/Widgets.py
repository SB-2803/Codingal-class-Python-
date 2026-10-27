#Import necessary libraries
from tkinter import *
from datetime import date

#Create window
root = Tk()
root.title('Getting started with widgets!!')
root.geometry('400x300')

#Add widgets and label
lbl = Label(text="Hey there!!", fg='white', bg="#152C71", height = 1, width=300)
#Add label for getting name as input from user and use entry widgets to create a text box for user to enter details
namelbl = Label(text="Full Name")
name_entry = Entry()

#Function to display a message
def display():
    #Read input given by user
    name = name_entry.get()
    global message,greet
    message = "Welcome to the Application!! \nToday's date is:"
    greet = "Hello"+name+"\n"
    #Specify where to add the details inside the text box
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

text_box = Text(height=3)

#Press button to call display function immediately
btn = Button(text="BEGIN", command=display, height=1)

#Organise all the widgets in the window
lbl.pack()
namelbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

#Start the GUI event loop
root.mainloop()