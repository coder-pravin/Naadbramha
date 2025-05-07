import tkinter as tk

def show_reports_page(container):
    for widget in container.winfo_children():
        widget.destroy()

    container.configure(bg="#f5f5f5")

    title = tk.Label(container, text="Reports Page", font=("Arial", 24), bg="#f5f5f5")
    title.pack(pady=30)

    # Example placeholder
    tk.Label(container, text="Coming Soon: Sales & Invoice Reports", font=("Arial", 14), bg="#f5f5f5").pack()
