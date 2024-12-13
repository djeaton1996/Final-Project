'''
BakeryBasket.py
Doniana Eaton
Intro to Software Development
12/13/24
This program is a bakery ordering system that allows users to add items to their cart, and then displays their total at the end.
'''

import tkinter as tk
from tkinter import messagebox

class BakeryBasket:
    def __init__(self, root):
        self.root = root
        self.root.title("Bakery Basket")

        # Initialize items and prices
        self.items = {
            "Bread": 2.50,
            "Croissant": 1.50,
            "Muffin": 1.75,
            "Cake Slice": 3.00,
            "Cookie": 0.75
        }

        # Initialize cart
        self.cart = {}

        # Header label
        tk.Label(self.root, text="Welcome to Bakery Basket!", font=("Arial", 16)).pack(pady=10)

        # Create a frame for the menu items
        menu_frame = tk.Frame(self.root)
        menu_frame.pack(pady=10)

        # Display menu items
        tk.Label(menu_frame, text="Menu", font=("Arial", 14)).grid(row=0, column=0, columnspan=2)

        row = 1
        for item, price in self.items.items():
            tk.Label(menu_frame, text=f"{item}: ${price:.2f}", font=("Arial", 12)).grid(row=row, column=0, sticky="w", padx=10)
            tk.Button(menu_frame, text="Add to Cart", command=lambda i=item: self.add_to_cart(i)).grid(row=row, column=1, padx=10)
            row += 1

        # Cart and Checkout
        tk.Label(self.root, text="Your Cart", font=("Arial", 14)).pack(pady=10)

        self.cart_text = tk.Text(self.root, width=40, height=10, state="disabled")
        self.cart_text.pack(pady=5)

        tk.Button(self.root, text="Checkout", command=self.checkout).pack(pady=10)

    def add_to_cart(self, item):
        """Adds an item to the cart."""
        if item in self.cart:
            self.cart[item] += 1
        else:
            self.cart[item] = 1

        self.update_cart()

    def update_cart(self):
        """Updates the cart display."""
        self.cart_text.configure(state="normal")
        self.cart_text.delete("1.0", tk.END)  # Clear current text

        total_price = 0
        for item, quantity in self.cart.items():
            price = self.items[item] * quantity
            total_price += price
            self.cart_text.insert(tk.END, f"{item} (x{quantity}): ${price:.2f}\n")

        self.cart_text.insert(tk.END, f"\nTotal: ${total_price:.2f}")
        self.cart_text.configure(state="disabled")

    def checkout(self):
        """Handles checkout functionality."""
        if not self.cart:
            messagebox.showinfo("Checkout", "Your cart is empty!")
            return

        total_price = sum(self.items[item] * quantity for item, quantity in self.cart.items())
        messagebox.showinfo("Checkout", f"Thank you for your order!\nYour total is: ${total_price:.2f}")

        # Clear the cart after checkout
        self.cart.clear()
        self.update_cart()

if __name__ == "__main__":
    root = tk.Tk()
    app = BakeryBasket(root)
    root.mainloop()
