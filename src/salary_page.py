# salary_page.py

import tkinter as tk

def show_salary_page(container):
    # Clear the existing widgets in the container
    for widget in container.winfo_children():
        widget.destroy()

    # Set background color for the container
    container.configure(bg="#f5f5f5")

    # Title label
    title = tk.Label(container, text="Salary Page", font=("Arial", 24), bg="#f5f5f5")
    title.pack(pady=30)

    # Placeholder label for salary content
    tk.Label(container, text="Coming Soon: Salary Details and Reports", font=("Arial", 14), bg="#f5f5f5").pack()

    # Example of a listbox or table that could show salary data
    tk.Label(container, text="Example Employee Salary Details", font=("Arial", 12), bg="#f5f5f5").pack(pady=10)

    # Example of a table layout (you can replace this with real data)
    salary_table = tk.Frame(container, bg="#f5f5f5")
    salary_table.pack(pady=10)

    columns = ["Employee ID", "Name", "Salary"]
    data = [
        ("001", "John Doe", "₹ 30,000"),
        ("002", "Jane Smith", "₹ 35,000"),
        ("003", "Alice Johnson", "₹ 40,000"),
    ]

    # Create table headers
    for col in columns:
        header = tk.Label(salary_table, text=col, font=("Arial", 12, "bold"), bg="#f5f5f5")
        header.grid(row=0, column=columns.index(col), padx=10, pady=5)

    # Create table rows with salary data
    for row_data in data:
        for col_idx, value in enumerate(row_data):
            cell = tk.Label(salary_table, text=value, font=("Arial", 12), bg="#f5f5f5")
            cell.grid(row=data.index(row_data) + 1, column=col_idx, padx=10, pady=5)
