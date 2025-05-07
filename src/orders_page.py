import tkinter as tk
from tkinter import ttk
import pandas as pd

def show_order_page(main_frame):
    # Clear existing widgets
    
    for widget in main_frame.winfo_children():
        widget.destroy()

    # Read the Excel file (replace with your file path)
    df = pd.read_excel(r"C:\path\to\your\orders.xlsx")  # Replace with your actual file path

    # Create a frame to display the order data
    orders_frame = tk.Frame(main_frame)
    orders_frame.pack(pady=20)

    # Treeview widget to display orders
    columns = list(df.columns)  # Get column names from Excel file
    tree = ttk.Treeview(orders_frame, columns=columns, show="headings")
    
    # Define headings
    for col in columns:
        tree.heading(col, text=col)
    
    # Insert rows from the dataframe
    for index, row in df.iterrows():
        tree.insert("", "end", values=list(row))
    
    tree.pack(fill="both", expand=True, padx=10, pady=10)

    # Adjust Treeview columns width
    for col in columns:
        tree.column(col, width=100)

    # Add a Scrollbar
    scrollbar = tk.Scrollbar(orders_frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

