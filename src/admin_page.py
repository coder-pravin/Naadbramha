import tkinter as tk
from tkinter import messagebox
from admin_dashboard import show_admin_dashboard

def show_admin_page(container):
    print("Admin Page Loaded")

    # Clear any existing widgets in the container
    for widget in container.winfo_children():
        widget.destroy()

    container.configure(bg="#f0f0f0")

    # Title for the page
    tk.Label(container, text="Admin Login", font=("Arial", 24, "bold"), bg="#f0f0f0").pack(pady=30)

    # Username label and input field
    tk.Label(container, text="Username:", font=("Arial", 14), bg="#f0f0f0").pack(pady=5)
    username_entry = tk.Entry(container, font=("Arial", 14))
    username_entry.pack(pady=10)

    # Password label and input field
    tk.Label(container, text="Password:", font=("Arial", 14), bg="#f0f0f0").pack(pady=5)
    password_entry = tk.Entry(container, font=("Arial", 14), show="*")
    password_entry.pack(pady=10)

    # Function to validate login
    def validate_login():
        username = username_entry.get()
        password = password_entry.get()

        # Simple username and password check (this can be enhanced with database checks)
        if username == "admin" and password == "admin123":
            messagebox.showinfo("Login Successful", "Welcome Admin!")
            show_admin_dashboard(container)  # Load Admin Dashboard if login is successful
        else:
            messagebox.showerror("Login Failed", "Invalid credentials. Please try again.")

    # Login button
    login_button = tk.Button(container, text="Login", font=("Arial", 14), bg="#4CAF50", fg="white", command=validate_login)
    login_button.pack(pady=20)

    return container
