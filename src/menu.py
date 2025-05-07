# menu.py - Fetching Menu Items from Database

import mysql.connector

def get_menu():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Pravyaa@143",
            database="naadbramha_db"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT item_id, item_name, price FROM menu")
        menu_items = cursor.fetchall()
        conn.close()
        return menu_items
    except mysql.connector.Error as err:
        print("Database Error:", err)
        return []


# database.py - Database Connection

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Pravyaa@143",
        database="naadbramha_db"
    )

# billing.py - Invoice Printing

def print_invoice(cart):
    if not cart:
        print("No items in cart to print.")
        return
    invoice_content = "==== Naadbramha Invoice ===="
    total = 0
    for item, details in cart.items():
        invoice_content += f"\n{item} x {details['qty']} = ₹{details['qty'] * details['price']}"
        total += details['qty'] * details['price']
    invoice_content += f"\nTotal: ₹{total}\nThank You for Visiting!"
    print(invoice_content)
print(get_menu())
# main.py - Updated to include these modules
