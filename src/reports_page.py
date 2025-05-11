import tkinter as tk
from tkinter import messagebox
import os
import platform
import subprocess
def reports(container):
    # Clear previous widgets
    for widget in container.winfo_children():
        widget.destroy()

    container.configure(bg="#fffef2")

    # Page Title
    title = tk.Label(container, text="Reports Dashboard", font=("Arial", 22, "bold"), bg="#fffef2", fg="#2e3f4f")
    title.pack(pady=20)

    # Description or instructions
    desc = tk.Label(container, text="View sales and performance reports generated from Excel dashboard.",
                    font=("Arial", 14), bg="#fffef2", fg="#444")
    desc.pack(pady=10)

    # Function to open the Excel dashboard
    def open_excel_dashboard():
        path = os.path.abspath("Data/Naadbrahma Expenses.xlsx")
        try:
            if platform.system() == "Windows":
                os.startfile(path)
            elif platform.system() == "Darwin":  # macOS
                subprocess.call(["open", path])
            else:  # Linux
                subprocess.call(["xdg-open", path])
        except Exception as e:
            messagebox.showerror("Error", f"Could not open dashboard:\n{e}")

    # Button to open dashboard
    tk.Button(
        container,
        text="Open Excel Dashboard",
        command=open_excel_dashboard,
        bg="#007acc",
        fg="white",
        font=("Arial", 14),
        padx=20,
        pady=10
    ).pack(pady=30)
