from tkinter import *
window = Tk()
window.title("Event Handler")
window.geometry("200x200")

def handle_keypressed(event):
    """Print the character associated to the key pressed"""
    print(event.char)
window.bind("<Key>", handle_keypressed)

def handle_click(event):
    print("\nThe Button was clicked!!")

button = Button(text="Click me:)")
button.pack()
button.bind("<Button-1>", handle_click)

window.mainloop()