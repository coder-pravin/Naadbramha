import tkinter as tk

def show_about_us_page(container):
    print("About Us Page Loaded")
    
    # Clear existing widgets from the container (main frame)
    for widget in container.winfo_children():
        widget.destroy()

    # Configure background color of the container
    container.configure(bg="#ffe5ec")

    # Title
    tk.Label(container, text="Welcome to Naadbramha Sales & Attendance System!", font=("Arial", 24, "bold"), bg="#ffe5ec").pack(pady=30)

    # Mission and Development Team Introduction
    intro_text = (
        "\"This application is developed by a passionate individual to simplifying\n"
        "sales tracking, billing, and staff attendance management.\"\n\n"
        "Our Mission:\n"
        "- Deliver simple and efficient business management solutions.\n"
        "- Support small and medium businesses with easy-to-use software.\n\n"
        "Development Team:\n"
        "- Pravyaa: Lead Developer & UI Designer\n"
        "- Assistant Developer: ChatGPT 😉\n\n"
        "Thank you for trusting us!"
    )

    tk.Label(container, text=intro_text, font=("Arial", 14), bg="#ffe5ec", justify="left").pack(pady=10)

    # Additional Contact or Help Text
    tk.Label(container, text="Feel free to contact us for further assistance.", font=("Arial", 14), bg="#ffe5ec").pack(pady=10)

    return container
