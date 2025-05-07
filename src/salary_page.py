# salary_page.py
import tkinter as tk
from tkinter import ttk, messagebox

# Dummy staff list (replace with DB fetch if needed)
staff_list = ["Staff001 - Ramesh", "Staff002 - Sita", "Staff003 - Ajay"]

def show_salary_page(parent):
    tk.Label(parent, text="Salary Management", font=("Arial", 18, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

    tk.Label(parent, text="Select Staff:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
    staff_combo = ttk.Combobox(parent, values=staff_list, width=30)
    staff_combo.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(parent, text="Monthly Salary (Rs):").grid(row=2, column=0, sticky="e", padx=5, pady=5)
    entry_salary = tk.Entry(parent)
    entry_salary.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(parent, text="Advance Taken (Rs):").grid(row=3, column=0, sticky="e", padx=5, pady=5)
    entry_advance = tk.Entry(parent)
    entry_advance.grid(row=3, column=1, padx=5, pady=5)

    tk.Label(parent, text="Remaining Balance:").grid(row=4, column=0, sticky="e", padx=5, pady=5)
    label_balance_val = tk.Label(parent, text="Rs. 0.00", fg="green")
    label_balance_val.grid(row=4, column=1, sticky="w", padx=5, pady=5)

    def calculate_balance():
        try:
            salary = float(entry_salary.get())
            advance = float(entry_advance.get())
            balance = salary - advance
            label_balance_val.config(text=f"Rs. {balance:.2f}")
        except ValueError:
            label_balance_val.config(text="Invalid input")

    def save_salary():
        staff = staff_combo.get()
        salary = entry_salary.get()
        advance = entry_advance.get()
        balance = label_balance_val.cget("text")

        if not staff or not salary or not advance:
            messagebox.showwarning("Incomplete Data", "Please fill all fields.")
            return

        # Replace with DB save logic
        messagebox.showinfo("Saved", f"Salary details saved for:\n{staff}\nBalance: {balance}")

    tk.Button(parent, text="Calculate Balance", command=calculate_balance).grid(row=5, column=1, sticky="e", pady=10)
    tk.Button(parent, text="Save", width=20, command=save_salary, bg="lightblue").grid(row=6, column=1, pady=10)
