from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os

root = Tk()
root.title('Denomination Calculator!!')
root.geometry('650x400')
root.configure(bg='light blue')

current_dir = os.path.dirname(__file__)
imagepath = os.path.join(current_dir, 'app_img.jpg')
upload = Image.open(imagepath)

upload = upload.resize((300,300))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg='light blue')
label.place(x=180, y=20)
label1= Label(root, text="Hey User!! Welcome to Denomination Counter Application :)", bg = 'light blue')
label1.place(relx=0.5, y=340, anchor=CENTER)

def msg():
    MsBox = messagebox.showinfo("Alert", "Do you want to calculate the denomination count?")
    if MsBox == "ok":
        topwin()

button1 = Button(root, text = "Let's get strated!!", command = msg, bg = 'brown', fg = 'white')
button1.place(x=260, y=360)

def topwin():
    top = Toplevel()
    top.title('Denomintaion Calculator!!')
    top.configure(bg='light grey')
    top.geometry('600x450')

    label = Label(top, text="Enter total amount", bg = 'light grey')
    entry=Entry(top)
    lbl=Label(top, text="Here are the number of notes for each denomination...", bg='light grey')
    l1 = Label(top, text="2000", bg="light grey")
    l2 = Label(top, text="500", bg="light grey")
    l3 = Label(top, text="100", bg="light grey")
    l4 = Label(top, text="50", bg="light grey")
    l5 = Label(top, text="20", bg="light grey")
    l6 = Label(top, text="10", bg="light grey")

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)
    t4 = Entry(top)
    t5 = Entry(top)
    t6 = Entry(top)

    def calculator():
        try:
            global amount
            amount = int(entry.get())
            note2000 = amount//2000
            amount %= 2000
            note500 = amount//500
            amount %= 500
            note100 = amount//100
            amount %= 100
            note50 = amount//50
            amount %= 50
            note20 = amount//20
            amount %= 20
            note10 = amount//10

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)
            t4.delete(0, END)
            t5.delete(0, END)
            t6.delete(0, END)

            t1.insert(END, str(note2000))
            t2.insert(END, str(note500))
            t3.insert(END, str(note100))
            t4.insert(END, str(note50))
            t5.insert(END, str(note20))
            t6.insert(END, str(note10))
        except ValueError:
            messagebox.showerror("Error!!", "Please enter a valid number.")

    btn = Button(top, text="Calculate", command = calculator, bg="brown", fg="white")

    label.place(x=230, y=50)
    entry.place(x=215, y=80)
    btn.place(x=180, y=150)
    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)
    l4.place(x=180, y=290)
    l5.place(x=180, y=320)
    l6.place(x=180, y=350)
    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)
    t4.place(x=270, y=290)
    t5.place(x=270, y=320)
    t6.place(x=270, y=350)

    top.mainloop()

root.mainloop()