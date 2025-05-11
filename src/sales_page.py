def sales_page(container):
    import tkinter as tk
    from tkinter import ttk, messagebox
    import mysql.connector
    from datetime import datetime

    # Clear current widgets
    for widget in container.winfo_children():
        widget.destroy()
    container.configure(bg="#fffef2")

    # Header
    header = tk.Label(container, text="Today's Sales", font=("Arial", 20, "bold"),
                      bg="#fffef2", fg="#2e3f4f")
    header.pack(pady=10)

    # Frame for table and total
    table_frame = tk.Frame(container, bg="#fffef2")
    table_frame.pack(fill="both", expand=True, padx=20, pady=10)

    # Treeview (sales table)
    columns = ("sale_id", "bill_id", "item_name", "price", "quantity", "total")
    tree = ttk.Treeview(table_frame, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col.replace("_", " ").title())
        tree.column(col, anchor="center", width=100)
    tree.pack(fill="both", expand=True)

    # Scrollbars
    vsb = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)
    vsb.pack(side="right", fill="y")

    # Total sales label
    total_sales_var = tk.StringVar(value="Total Sales: ₹ 0.00")
    total_label = tk.Label(container, textvariable=total_sales_var, font=("Arial", 14, "bold"),
                           bg="#fffef2", fg="#333")
    total_label.pack(pady=5)

    # Load today's sales from DB
    def load_sales():
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Pravyaa@143",
                database="naadbramha_db"
            )
            cursor = conn.cursor()
            cursor.execute("""
                SELECT "sale_id", "bill_id", "item_name", "price", "quantity", "total"
                FROM sales 
                
            """)
            rows = cursor.fetchall()
            conn.close()

            for row in rows:
                tree.insert("", "end", values=row)

            total = sum(float(r[4]) for r in rows)
            today = datetime.now().strftime('%Y-%m-%d')
            total_sales_var.set(f"Today's Total Sales ({today}): ₹ {total:.2f}")

        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    load_sales()
