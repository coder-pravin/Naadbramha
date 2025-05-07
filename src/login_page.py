import tkinter as tk
from tkinter import messagebox

# Function to show the login page
def show_login_page(parent, on_successful_login):
    frame = tk.Frame(parent, bg="#f8f9fa")

    login_frame = tk.Frame(parent, bg="#fffef2", padx=30, pady=40)
    login_frame.place(relx=0.5, rely=0.5, anchor="center")  # Center the frame

    # Title Label
    tk.Label(login_frame, text="Naadbramha Login", font=("Arial", 24, "bold"), bg="#fffef2", fg="#4CAF50").grid(row=1, column=0, columnspan=2, pady=10)

    # Username and Password Labels and Entry fields
    tk.Label(login_frame, text="Username:", font=("Arial", 12), bg="#fffef2").grid(row=2, column=0, sticky="e", pady=5)
    username_entry = tk.Entry(login_frame, font=("Arial", 12), width=30)
    username_entry.grid(row=2, column=1, pady=5)

    tk.Label(login_frame, text="Password:", font=("Arial", 12), bg="#fffef2").grid(row=3, column=0, sticky="e", pady=5)
    password_entry = tk.Entry(login_frame, font=("Arial", 12), show="*", width=30)
    password_entry.grid(row=3, column=1, pady=5)

    # Error message label (hidden initially)
    error_label = tk.Label(login_frame, text="", font=("Arial", 10), fg="red", bg="#fffef2")
    error_label.grid(row=4, column=0, columnspan=2, pady=5)

    # Login button
    def check_login():
        username = username_entry.get()
        password = password_entry.get()

        if username == "staff" and password == "pass@123":
            messagebox.showinfo("Login Successful", "Welcome to Naadbramha!")
            login_frame.destroy()  # Close the login page
            on_successful_login()  # Open the admin dashboard
        else:
            error_label.config(text="Invalid username or password!")

    login_button = tk.Button(login_frame, text="Login", font=("Arial", 12), command=check_login, bg="#4CAF50", fg="white", width=20, height=2)
    login_button.grid(row=5, column=0, columnspan=2, pady=20)

# Function to show the admin dashboard
def show_admin_dashboard(parent):
    frame = tk.Frame(parent, bg="#f8f9fa")
    
    # Example admin dashboard content
    tk.Label(frame, text="Admin Dashboard", font=("Arial", 24, "bold"), bg="#f8f9fa", fg="#4CAF50").pack(pady=20)

    tk.Label(frame, text="Welcome, Admin!", font=("Arial", 16), bg="#f8f9fa").pack(pady=20)

    # Add your admin functionalities here
    # For example, buttons for different admin tasks
    tk.Button(frame, text="Manage Users", font=("Arial", 14), bg="#4CAF50", fg="white").pack(pady=10)
    tk.Button(frame, text="View Orders", font=("Arial", 14), bg="#4CAF50", fg="white").pack(pady=10)

    frame.pack(fill="both", expand=True)
    parent.geometry("1024x600")
    parent.state("zoomed")
    parent.title("Naadbramha - Admin Dashboard")

# Main application window
root = tk.Tk()
root.geometry("1024x600")
root.state("zoomed")
root.title("Naadbramha - Sales & Attendance System")

# Function to show the main page with an Admin tab
def show_main_page():
    main_frame = tk.Frame(root, bg="#f8f9fa")
    
    # Create a tab for Admin
    admin_button = tk.Button(main_frame, text="Admin", font=("Arial", 14), bg="#4CAF50", fg="white", command=lambda: show_login_page(root, show_admin_dashboard))
    admin_button.pack(pady=20)

    main_frame.pack(fill="both", expand=True)

# Show the main page initially
show_main_page()

# Run the application
root.mainloop()
