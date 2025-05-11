import tkinter as tk
from attendance_page import show_attendance_page  # Make sure this file exists and is correct
from inventory_page import record_inventory_page
from salary_page import show_salary_page
from logout import perform_logout
from sales_page import sales_page
from reports_page import reports
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
        reports(content_frame)

    def show_attendance():
        clear_content()
        show_attendance_page(content_frame)

    def show_sales():
        clear_content()
        sales_page(content_frame)


    def show_inventory():
        clear_content()
        record_inventory_page(content_frame)
    def show_salary():
        clear_content()
        show_salary_page(content_frame)
    def logout():
        perform_logout(container)
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
    
    show_attendance_page(content_frame)