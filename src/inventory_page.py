import tkinter as tk
from tkinter import ttk  # for Combobox
import mysql.connector
import pandas as pd
from datetime import datetime

def record_inventory_page(container):
    for widget in container.winfo_children():
        widget.destroy()

    container.configure(bg="#fffef2")

    tk.Label(container, text="Inventory Management", font=("Arial", 24), bg="#fffef2").pack(pady=30)
    tk.Label(container, text="Record Raw Materials Ordered", font=("Arial", 14), bg="#fffef2").pack(pady=10)

    form_frame = tk.Frame(container, bg="#fffef2")
    form_frame.pack(pady=20)

    tk.Label(form_frame, text="Item Name:", font=("Arial", 12), bg="#fffef2").grid(row=0, column=0, pady=5, sticky="e")

    # Create ComboBox for selecting inventory item
    inventory_items = [
        "Chutney", "Coconut", "Foil Paper", "Plastic Bags", "Oil", "Sambhar Masala",
        "Idli Rawa", "Gas Cylinder", "Cleaning Liquid", "Tissue Paper"
    ]

    item_name_combo = ttk.Combobox(form_frame, values=inventory_items, font=("Arial", 12))
    item_name_combo.grid(row=0, column=1, pady=5, padx=10)
    item_name_combo.set("Select Item")  # default text

    tk.Label(form_frame, text="Quantity Ordered:", font=("Arial", 12), bg="#fffef2").grid(row=1, column=0, pady=5, sticky="e")
    quantity_entry = tk.Entry(form_frame, font=("Arial", 12))
    quantity_entry.grid(row=1, column=1, pady=5, padx=10)

    tk.Label(form_frame, text="Order Date:", font=("Arial", 12), bg="#fffef2").grid(row=2, column=0, pady=5, sticky="e")
    date_entry = tk.Entry(form_frame, font=("Arial", 12))
    date_entry.grid(row=2, column=1, pady=5, padx=10)

    today_date = datetime.now().strftime("%Y-%m-%d")
    date_entry.insert(0, today_date)

    def save_order():
        item_name = item_name_combo.get()
        quantity = quantity_entry.get()
        order_date = date_entry.get()

        # Save to MySQL
        conn = mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="Pravyaa@143",
            database="naadbramha_db"
        )
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS inventory_orders (
                id INT AUTO_INCREMENT PRIMARY KEY,
                item_name VARCHAR(255) NOT NULL,
                quantity VARCHAR(255) NOT NULL,
                order_date DATE NOT NULL
            )
        ''')

        insert_query = '''
            INSERT INTO inventory_orders (item_name, quantity, order_date)
            VALUES (%s, %s, %s)
        '''
        values = (item_name, quantity, order_date)
        cursor.execute(insert_query, values)

        conn.commit()
        conn.close()

        print("Order saved to MySQL database!")

        item_name_combo.set("Select Item")
        quantity_entry.delete(0, tk.END)

    def export_to_excel():
        conn = mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password",
            database="your_database"
        )
        df = pd.read_sql("SELECT * FROM inventory_orders", conn)
        df.to_excel("inventory_orders.xlsx", index=False)
        conn.close()
        print("Exported MySQL orders to Excel!")

    save_button = tk.Button(container, text="Save Order", font=("Arial", 12), command=save_order, bg="#ffb347", fg="white")
    save_button.pack(pady=10)

    export_button = tk.Button(container, text="Export to Excel", font=("Arial", 12), command=export_to_excel, bg="#4CAF50", fg="white")
    export_button.pack(pady=10)
