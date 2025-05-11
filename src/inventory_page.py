def record_inventory_page(container):
    from tkinter import ttk, messagebox
    import mysql.connector
    import pandas as pd
    import tkinter as tk
    import os
    from datetime import datetime
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A6

    for widget in container.winfo_children():
        widget.destroy()
    container.configure(bg="#fffef2")

    title = tk.Label(container, text="Inventory Management", font=("Arial", 20, "bold"), bg="#fffef2", fg="#2e3f4f")
    title.pack(pady=10)

    main_frame = tk.Frame(container, bg="#fffef2")
    main_frame.pack(fill="both", expand=True, padx=20, pady=10)

    # ---------- LEFT SIDE ----------
    left_frame = tk.Frame(main_frame, bg="#fffef2", width=400)
    left_frame.pack(side="left", fill="y", padx=10, pady=10)

    tk.Label(left_frame, text="Order Inventory Items", font=("Arial", 16, "bold"), bg="#fffef2").pack(pady=10)

    inventory_items = [
        "Chutney", "Coconut", "Foil Paper", "Plastic Bags", "Oil", "Sambhar Masala",
        "Idli Rawa", "Gas Cylinder", "Cleaning Liquid", "Tissue Paper"
    ]
    item_var = tk.StringVar(value="Select Item")
    qty_var = tk.StringVar()

    ttk.Label(left_frame, text="Item:", font=("Arial", 12)).pack(anchor="w", padx=5)
    item_combo = ttk.Combobox(left_frame, values=inventory_items, textvariable=item_var, font=("Arial", 12), width=30)
    item_combo.pack(pady=5)

    ttk.Label(left_frame, text="Quantity:", font=("Arial", 12)).pack(anchor="w", padx=5)
    qty_entry = tk.Entry(left_frame, textvariable=qty_var, font=("Arial", 12), width=32)
    qty_entry.pack(pady=5)

    order_list = []

    def add_item():
        item = item_var.get()
        qty = qty_var.get()
        if item == "Select Item" or not qty:
            messagebox.showwarning("Missing Data", "Please select an item and enter quantity.")
            return
        order_list.append((item, qty))
        update_summary()
        item_var.set("Select Item")
        qty_var.set("")

    tk.Button(left_frame, text="Add Item", command=add_item, bg="#ffb347", fg="white", font=("Arial", 12), width=20).pack(pady=10)

    # ---------- RIGHT SIDE ----------
    right_frame = tk.Frame(main_frame, bg="#fffef2")
    right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

    tk.Label(right_frame, text="Order Summary", font=("Arial", 16, "bold"), bg="#fffef2").pack(pady=(10, 5))
    
    # Summary Text Box Frame
    summary_frame = tk.Frame(right_frame, bg="#fffef2")
    summary_frame.pack(fill="both", expand=True, padx=10, pady=(0, 5))

    summary_box = tk.Text(summary_frame, height=20, font=("Arial", 12), wrap="word", relief="solid", borderwidth=1)
    summary_box.pack(fill="both", expand=True)
    summary_box.config(state="disabled")

    # Save Button Frame
    button_frame = tk.Frame(right_frame, bg="#fffef2")
    button_frame.pack(pady=(0, 15))

    def update_summary():
        summary_box.config(state="normal")
        summary_box.delete("1.0", tk.END)
        for idx, (item, qty) in enumerate(order_list, start=1):
            summary_box.insert(tk.END, f"{idx}. {item} - Qty: {qty}\n")
        summary_box.config(state="disabled")

    def save_order():
        if not order_list:
            messagebox.showwarning("Empty", "No items to save.")
            return

        # Save to MySQL
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Pravyaa@143",
                database="naadbramha_db"
            )
            cursor = conn.cursor()
            cursor.execute(''' 
                CREATE TABLE IF NOT EXISTS inventory_ordered (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    item_name VARCHAR(255),
                    quantity VARCHAR(255),
                    order_date DATE
                )
            ''')
            today = datetime.now().strftime('%Y-%m-%d')
            for item, qty in order_list:
                cursor.execute("INSERT INTO inventory_ordered (item_name, quantity, order_date) VALUES (%s, %s, %s)",
                               (item, qty, today))
            conn.commit()
            cursor.close()
            conn.close()
        except Exception as e:
            messagebox.showerror("Database Error", str(e))
            return

        # Save PDF
        try:
            os.makedirs("invoices", exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            pdf_file = f"invoices/Inventory_Order_{timestamp}.pdf"
            c = canvas.Canvas(pdf_file, pagesize=A6)
            c.setFont("Helvetica", 10)
            c.drawString(10, 220, "Naadbramha Inventory Order Summary")
            c.drawString(10, 205, f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
            y = 190
            c.drawString(10, y, "Item".ljust(20) + "Quantity")
            y -= 10
            for i, (item, qty) in enumerate(order_list, 1):
                c.drawString(10, y, f"{i}. {item.ljust(20)} {qty}")
                y -= 15
            c.save()

            # Attempt to print the PDF
            try:
                os.startfile(pdf_file, "print")  # Windows-only printing
            except Exception as e:
                messagebox.showerror("PDF Error", f"Could not send to printer: {e}")

            messagebox.showinfo("Saved", f"Order saved & PDF generated:\n{pdf_file}")
        except Exception as e:
            messagebox.showerror("PDF Error", str(e))

        order_list.clear()
        update_summary()

    # Save & Print Button
    save_print_btn = tk.Button(button_frame, text="Save & Print", command=save_order, bg="#6ac29e", fg="white", font=("Arial", 12), width=20)
    save_print_btn.pack(pady=10)
