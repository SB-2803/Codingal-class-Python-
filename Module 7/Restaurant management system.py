import tkinter as tk
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

        for i, (item, price) in enumerate(self.menu_items.items(), start=1):
            label = ttk.Label(frame, text=f"{item} (₹{price}):", font=("Arial", 12))
            label.grid(row=i, column=0, padx=10, pady=5)

            quantity_entry = ttk.Entry(frame, width=5)
            quantity_entry.grid(row=i, column=1, padx=10, pady=5) 
            self.menu_quantities[item] = quantity_entry

        order_button = ttk.Button(frame, text="Place Order", command=self.place_order)
        order_button.grid(row=len(self.menu_items)+1, columnspan=2, padx=10, pady=10)

    def setup_background(self, root):
        bgwidth, bgheight = 800, 600
        canvas = tk.Canvas(root, width=bgwidth, height=bgheight)
        canvas.pack()
        current_dir = os.path.dirname(__file__)
        image_path = os.path.join(current_dir, "restaurant.png")
        pil_img = Image.open(image_path)
        pil_img = pil_img.resize((bgwidth, bgheight))
        self.background_image = ImageTk.PhotoImage(pil_img)
        canvas.create_image(0, 0, anchor = tk.NW, image = self.background_image)
        canvas.image = self.background_image

    def place_order(self):
        total_cost = 0
        order_summary = "Order Summary"

        for item, entry in self.menu_quantities.items():
            quantity = entry.get()
            if quantity.isdigit():
                quantity = int(quantity)
                price = self.menu_items[item]
                cost = quantity * price
                total_cost += cost
                if quantity > 0:
                    order_summary += (f"\n{item}: {quantity} x ₹{price} = ₹{cost}")

        if total_cost > 0:
                order_summary += f"\nTotal Cost: ₹{total_cost}"
                messagebox.showinfo("Order Placed", order_summary)
        else:
                messagebox.showerror("Error", "Please order at least one item.")

if __name__ == "__main__":
    root=tk.Tk()
    app = RestaurantMangaementSystem(root)
    root.geometry("800x600")
    root.mainloop()