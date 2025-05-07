import tkinter as tk
from PIL import Image, ImageTk
from home_page import show_home_page
from inventory_page import record_inventory_page
from admin_page import show_admin_page
from about_us_page import show_about_us_page

root = tk.Tk()
root.geometry("1024x600")
root.state("zoomed")
root.title("Naadbramha - Sales & Attendance System")
root.iconbitmap("Images/naadbramha.ico")

# Create the navigation bar frame
nav_frame = tk.Frame(root, bg="#343a40", height=50)
nav_frame.pack(side="top", fill="x")

# Create the main content frame
main_frame = tk.Frame(root, bg="cyan")
main_frame.pack(side="top", fill="both", expand=True)

# Function to load frames dynamically
def show_frame(frame_func):
    # Clear existing widgets from the main frame
    for widget in main_frame.winfo_children():
        widget.destroy()
    # Load the new frame
    page = frame_func(main_frame)
    page.pack(fill="both", expand=True)

# Define navigation buttons
nav_buttons = [
    ("Home", show_home_page),
    ("Admin", show_admin_page),
    ("About Us",show_about_us_page)
    ]

# Create and pack navigation buttons
for label, func in nav_buttons:
    btn = tk.Button(
        nav_frame,
        text=label,
        bg="#343a40",
        fg="white",
        bd=0,
        padx=20,
        pady=10,
        font=("Arial", 12,),
        command=lambda f=func: show_frame(f)
    )
    btn.pack(side="left")

# Load the default page
show_frame(show_home_page)

# Start the main event loop
root.mainloop()
