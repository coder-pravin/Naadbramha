import tkinter as tk
from tkinter import ttk, messagebox
from menu import get_menu
from menu import print_invoice as billing_print_invoice

def show_home_page(parent):
    frame = tk.Frame(parent, bg="#f8f9fa")

    cart = {}

    def add_to_cart(item_name, price, quantity):
        if item_name in cart:
            cart[item_name]["qty"] += quantity
        else:
            cart[item_name] = {"price": price, "qty": quantity}
        refresh_invoice()

    def refresh_invoice():
        for item in invoice_list.get_children():
            invoice_list.delete(item)
        for item, details in cart.items():
            total_price = details["price"] * details["qty"]
            invoice_list.insert("", "end", values=(item, details["qty"], f"₹{total_price}"))

    def print_invoice_action():
        if not cart:
            messagebox.showwarning("Warning", "Invoice is empty!")
            return
        billing_print_invoice(cart)
        messagebox.showinfo("Success", "Invoice sent to printer!")
        cart.clear()
        refresh_invoice()


    # --- Left Section: Menu List ---
    menu_frame = tk.Frame(frame, bg="#ffffff", padx=20, pady=20)
    menu_frame.pack(side="left", fill="y", padx=10, pady=10)

    tk.Label(menu_frame, text="Naadbramha's Menu", font=("Arial", 18, "bold"), bg="white", fg="black").pack(pady=10)

    menu_canvas = tk.Canvas(menu_frame, height=500, width=700, bg="white")
    scrollbar = tk.Scrollbar(menu_frame, orient="vertical", command=menu_canvas.yview)
    scrollable_frame = tk.Frame(menu_canvas, bg="white")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: menu_canvas.configure(scrollregion=menu_canvas.bbox("all"))
    )

    menu_canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    menu_canvas.configure(yscrollcommand=scrollbar.set)

    def on_mousewheel(event):
        menu_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    menu_canvas.bind_all("<MouseWheel>", on_mousewheel)
    menu_canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    def on_enter(e):
        e.widget.config(bg="#e0f7fa")

    def on_leave(e):
        e.widget.config(bg="white")

    for item_id, item_name, price in get_menu():
        item_frame = tk.Frame(scrollable_frame, bg="white", bd=2, relief="groove", padx=10, pady=10, width=600, height=100)
        item_frame.pack(pady=5)
        item_frame.pack_propagate(False)

        item_frame.bind("<Enter>", on_enter)
        item_frame.bind("<Leave>", on_leave)

        # Row layout: label left, controls right
        content_frame = tk.Frame(item_frame, bg="white")
        content_frame.pack(fill="both", expand=True)

        tk.Label(content_frame, text=f"{item_name} - ₹{price}", font=("Arial", 16), bg="white").pack(side="left", anchor="w", padx=5)

        qty_var = tk.IntVar(value=1)
        control_frame = tk.Frame(content_frame, bg="white")
        control_frame.pack(side="right", anchor="e")

        tk.Spinbox(control_frame, from_=1, to=99, width=3, textvariable=qty_var, font=("Arial", 12)).pack(side="right", padx=5)
        tk.Button(control_frame, text="Add", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white",
                  command=lambda name=item_name, pr=price, qv=qty_var: add_to_cart(name, pr, qv.get())
                  ).pack(side="right", padx=5)

    # --- Right Section: Invoice List ---
    invoice_frame = tk.Frame(frame, bg="#ffffff", width=450, padx=20, pady=20)
    invoice_frame.pack(side="right", fill="y", padx=10, pady=10)
    invoice_frame.pack_propagate(False)

    tk.Label(invoice_frame, text="Invoice", font=("Arial", 18, "bold"), bg="#4CAF50", fg="white").pack(pady=10)

    columns = ("Item", "Quantity", "Price")
    invoice_list = ttk.Treeview(invoice_frame, columns=columns, show="headings", height=15)

    invoice_list.heading("Item", text="Item")
    invoice_list.heading("Quantity", text="Quantity")
    invoice_list.heading("Price", text="Price")

    invoice_list.column("Item", width=150, anchor="w")
    invoice_list.column("Quantity", width=50, anchor="center")
    invoice_list.column("Price", width=70, anchor="center")

    invoice_list.pack(fill="both", expand=True, padx=10, pady=10)

    # Buttons
    tk.Button(invoice_frame, text="Print Invoice", font=("Arial", 14, "bold"), bg="#4CAF50", fg="white",
              command=print_invoice_action).pack(pady=10)

    tk.Button(invoice_frame, text="Clear Cart", font=("Arial", 14, "bold"), bg="#dc3545", fg="white",
              command=lambda: [cart.clear(), refresh_invoice()]).pack(pady=5)

    return frame
