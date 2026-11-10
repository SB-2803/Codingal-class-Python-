from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

window = Tk()
window.title("Codingal's Text Editor!!")
window.geometry("600x500")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

def open_file():
    #Open a file for editing
    filepath =  askopenfilename(filetype=[("Text Files", "*.txt"),("All Files", "*.*")])
    if not filepath:
        return
    txt_edit.delete(1.0,END)
    #If a file is opened then display the contents of the file without editing, in the text editor box
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(END,text)
        input_file.close()
    window.title(f"Codingal's Text Editor - {filepath}")

def save_file():
    #Save the current file as a new file where you can edit, display the function(hence, write)
    filepath = asksaveasfilename(defaultextension="txt", filetypes=[("Text Files", "*.txt"),("All Files","*.*")])
    if not filepath:
        return
    with open(filepath, "w") as output_file:
            text = txt_edit.get(1.0, END)
            output_file.write(text)
    window.title(f"Codingal's Text Editor - {filepath}")    

txt_edit = Text(window)
fr_buttons = Frame(window, relief=RAISED, bd=2)
btn_open = Button(fr_buttons, text ="Open", command = open_file)
btn_save = Button(fr_buttons, text ="Save As...", command = save_file)
btn_open.grid(row=0, column=0, sticky="ew", pady=5, padx=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()