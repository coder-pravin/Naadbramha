import tkinter as tk
from attendance_page import show_attendance_page  # Make sure this file exists and is correct
from inventory_page import record_inventory_page
def show_admin_dashboard(container):
    # Clear any existing content in the main container
    for widget in container.winfo_children():
        widget.destroy()

    container.configure(bg="#f0f0f0")

    # --- Navigation Frame at the top ---
    nav_frame = tk.Frame(container,)
    nav_frame.pack(side="top", fill="x", pady=10)

    # --- Content Frame where pages will be shown ---
    content_frame = tk.Frame(container, bg="#ffffff", relief="ridge", bd=2)
    content_frame.pack(fill="both", expand=True, padx=10, pady=10)

    def clear_content():
        for widget in content_frame.winfo_children():
            widget.destroy()

    # --- Section Functions ---
    def show_reports():
        clear_content()
        tk.Label(content_frame, text="Reports Page", font=("Arial", 18)).pack(pady=50)

    def show_attendance():
        clear_content()
        show_attendance_page(content_frame)

    def show_sales():
        clear_content()
        tk.Label(content_frame, text="Sales Page", font=("Arial", 18)).pack(pady=50)

    def show_inventory():
        clear_content()
        record_inventory_page(content_frame)
    def show_salary():
        clear_content()
        tk.Label(content_frame, text="Salary Page", font=("Arial", 18)).pack(pady=50)

    def logout():
        print("Logging out...")
    tk.Label(nav_frame, text="Admin Dashboard", font=("Arial", 18, "bold"), bg="#dfefff").pack(side="right", padx=15)

    # --- Create buttons in nav_frame (horizontal layout) ---
    buttons = [
        ("Reports", show_reports),
        ("Attendance", show_attendance),
        ("Sales", show_sales),
        ("Inventory",show_inventory),
        ("Salary", show_salary),
        ("Logout", logout)
    ]

    for label, command in buttons:
        tk.Button(nav_frame, text=label, width=15, height=2, command=command).pack(side="left", padx=5)
        
