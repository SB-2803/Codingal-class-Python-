from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("200x200")

#Function for displaying warning that will be called once button is clicked.
#messagebox.showwarining("window.name", text to be displayed)
def msg():
    messagebox.showwarning("Alert!!", "Stop!!! Virus found...")

button = Button(root, text="Scan for Virus...", command=msg)
button.place(x=40, y=40)

root.mainloop()