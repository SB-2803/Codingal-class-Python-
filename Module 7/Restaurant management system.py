from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os

class RestaurantMangaementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Management App!!")
        self.menu_items = {
            "Fries": 165,
            "Sandwich": 165,
            "Burger": 250,
            "Pizza": 350,
            "Pasta": 285,
            "Cold Coffee": 85,
            "Macha": 120
        }

        self.setup_background(root)
        frame = ttk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        ttk.Label(frame,text="Restaurant Management System", font=("Arial", 20, "bold")).grid(row=0, columnspan=2, padx=10, pady=10)
        self.menu_quantities = {}
        