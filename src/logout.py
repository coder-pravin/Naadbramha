# logout.py
from tkinter import messagebox
from home_page import show_home_page  # Make sure this file and function exist
from home_page import show_home_page

def perform_logout(container):
    confirm = messagebox.askyesno("Logout", "Are you sure you want to logout?")
    if confirm:
        for widget in container.winfo_children():
            widget.destroy()
        show_home_page(container).pack(fill="both", expand=True)
