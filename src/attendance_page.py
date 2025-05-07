import tkinter as tk
import mysql.connector
from datetime import datetime

def mark_attendance(staff_id, status, refresh_callback):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Pravyaa@143",  # Update if needed
        database="naadbramha_db"
    )
    cursor = conn.cursor()

    today = datetime.now().date()

    cursor.execute("SELECT * FROM attendance WHERE staff_id=%s AND date=%s", (staff_id, today))
    result = cursor.fetchone()

    if result:
        cursor.execute("UPDATE attendance SET status=%s WHERE staff_id=%s AND date=%s", (status, staff_id, today))
    else:
        cursor.execute("INSERT INTO attendance (staff_id, date, status) VALUES (%s, %s, %s)", (staff_id, today, status))

    conn.commit()
    conn.close()
    refresh_callback()

# Function to mark attendance in DB
def show_attendance_page(container):
    for widget in container.winfo_children():
        widget.destroy()

    container.configure(bg="#f0f9ff")

    tk.Label(container, text="Staff Attendance Page", font=("Helvetica", 18, "bold"), bg="#f0f9ff", fg="#003366").pack(pady=20, anchor="c", padx=20)

    # --- Scrollable Canvas Setup ---
    canvas = tk.Canvas(container, bg="#f0f9ff", highlightthickness=0)
    scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#f0f9ff")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True, padx=10, pady=10)
    scrollbar.pack(side="right", fill="y", pady=10)

    # --- Mouse Wheel Event for Scrolling ---
    def on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    # Bind mouse wheel event to canvas
    canvas.bind_all("<MouseWheel>", on_mousewheel)

    # --- Database Fetching ---
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Pravyaa@143",
        database="naadbramha_db"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT staff_id, name, mobile, role FROM staff")
    staff_list = cursor.fetchall()
    conn.close()

    today = datetime.now().date()
    attendance_status = {}

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Pravyaa@143",
        database="naadbramha_db"
    )
    cur = conn.cursor()
    cur.execute("SELECT staff_id, status FROM attendance WHERE date=%s", (today,))
    for sid, status in cur.fetchall():
        attendance_status[sid] = status
    conn.close()

    # --- Create UI Cards ---
    for staff_id, name, mobile, role in staff_list:
        card = tk.Frame(scrollable_frame, bg="white", bd=2, relief="groove", padx=10, pady=10)
        card.pack(pady=8, padx=20, fill="x", expand=True)

        tk.Label(card, text=f"Name: {name}", font=("Helvetica", 14, "bold"), bg="white").grid(row=0, column=0, sticky="w")
        tk.Label(card, text=f"Mobile: {mobile}", font=("Helvetica", 12), bg="white").grid(row=1, column=0, sticky="w")
        tk.Label(card, text=f"Role: {role}", font=("Helvetica", 12), bg="white").grid(row=1, column=1, sticky="w", padx=10)
        tk.Label(card, text=f"ID: {staff_id}", font=("Helvetica", 12), bg="white").grid(row=0, column=1, sticky="w", padx=10)

        current_status = attendance_status.get(staff_id, "Not Marked")
        status_color = {
            "Present": "green",
            "Absent": "red",
            "Leave": "orange",
            "Not Marked": "gray"
        }.get(current_status, "gray")

        status_label = tk.Label(card, text=f"Status: {current_status}", font=("Helvetica", 12, "italic"), fg=status_color, bg="white")
        status_label.grid(row=0, column=2, padx=15)

        # Attendance Buttons
        tk.Button(card, text="Present", font=("Helvetica", 11), bg="#d4edda", fg="green",
                  command=lambda s=staff_id: mark_attendance(s, "Present", lambda: show_attendance_page(container))
                  ).grid(row=2, column=0, pady=10)

        tk.Button(card, text="Absent", font=("Helvetica", 11), bg="#f8d7da", fg="red",
                  command=lambda s=staff_id: mark_attendance(s, "Absent", lambda: show_attendance_page(container))
                  ).grid(row=2, column=1, pady=10, padx=10)

        tk.Button(card, text="Leave", font=("Helvetica", 11), bg="#fff3cd", fg="orange",
                  command=lambda s=staff_id: mark_attendance(s, "Leave", lambda: show_attendance_page(container))
                  ).grid(row=2, column=2, pady=10, padx=10)
