import tkinter as tk
from tkinter import ttk, messagebox
import csv

students = []

# Grade function
def calculate_grade(avg):
    if avg >= 90:
        return "O"
    elif avg >= 80:
        return "E"
    elif avg >= 70:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "D"

# Update stats
def update_stats():
    if not students:
        topper_label.config(text="🥇 Topper: ")
        lowest_label.config(text="⚠️ Lowest: ")
        return

    topper = max(students, key=lambda x: x["avg"])
    lowest = min(students, key=lambda x: x["avg"])

    topper_label.config(text=f"🥇 Topper: {topper['name']} ({topper['avg']:.2f})")
    lowest_label.config(text=f"⚠️ Lowest: {lowest['name']} ({lowest['avg']:.2f})")

# Add student
def add_student():
    try:
        name = name_entry.get()
        marks = list(map(float, marks_entry.get().split(",")))

        total = sum(marks)
        avg = total / len(marks)
        grade = calculate_grade(avg)

        student = {"name": name, "total": total, "avg": avg, "grade": grade}
        students.append(student)

        tree.insert("", "end", values=(name, f"{total:.2f}", f"{avg:.2f}", grade))

        update_stats()

        name_entry.delete(0, tk.END)
        marks_entry.delete(0, tk.END)

    except:
        messagebox.showerror("Error", "Please enter valid data!")

# Delete student
def delete_student():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Warning", "Select a student to delete!")
        return

    for item in selected:
        values = tree.item(item, "values")
        name = values[0]

        # Remove from list
        for s in students:
            if s["name"] == name:
                students.remove(s)
                break

        tree.delete(item)

    update_stats()

# Save to CSV
def save_csv():
    if not students:
        messagebox.showwarning("Warning", "No data to save!")
        return

    with open("students_report.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Total", "Average", "Grade"])

        for s in students:
            writer.writerow([s["name"], f"{s['total']:.2f}", f"{s['avg']:.2f}", s["grade"]])

    messagebox.showinfo("Success", "Data saved as students_report.csv")

# ================= GUI =================

root = tk.Tk()
root.title("🎓 Student Analytics Dashboard")
root.geometry("800x600")
root.config(bg="#1e1e2f")

title = tk.Label(root, text="Student Analytics Dashboard",
                 bg="#1e1e2f", fg="#00ffcc",
                 font=("Helvetica", 22, "bold"))
title.pack(pady=10)

frame = tk.Frame(root, bg="#1e1e2f")
frame.pack(pady=10)

tk.Label(frame, text="Student Name:", bg="#1e1e2f",
         fg="white", font=("Arial", 13)).grid(row=0, column=0, padx=10, pady=5)

name_entry = tk.Entry(frame, font=("Arial", 13), width=22)
name_entry.grid(row=0, column=1)

tk.Label(frame, text="Marks (comma separated):", bg="#1e1e2f",
         fg="white", font=("Arial", 13)).grid(row=1, column=0, padx=10, pady=5)

marks_entry = tk.Entry(frame, font=("Arial", 13), width=22)
marks_entry.grid(row=1, column=1)

# Buttons Frame
btn_frame = tk.Frame(root, bg="#1e1e2f")
btn_frame.pack(pady=10)

add_btn = tk.Button(btn_frame, text="➕ Add",
                    command=add_student,
                    bg="#00ffcc", fg="black",
                    font=("Arial", 12, "bold"), width=12)
add_btn.grid(row=0, column=0, padx=10)

delete_btn = tk.Button(btn_frame, text="🗑️ Delete",
                       command=delete_student,
                       bg="#ff4d4d", fg="white",
                       font=("Arial", 12, "bold"), width=12)
delete_btn.grid(row=0, column=1, padx=10)

save_btn = tk.Button(btn_frame, text="💾 Save CSV",
                     command=save_csv,
                     bg="#4da6ff", fg="white",
                     font=("Arial", 12, "bold"), width=12)
save_btn.grid(row=0, column=2, padx=10)

# Table style
style = ttk.Style()
style.theme_use("default")

style.configure("Treeview",
                background="#2e2e3f",
                foreground="white",
                rowheight=32,
                fieldbackground="#2e2e3f",
                font=("Arial", 12))

style.configure("Treeview.Heading",
                font=("Arial", 14, "bold"),
                background="#00ffcc",
                foreground="black")

tree = ttk.Treeview(root,
                    columns=("Name", "Total", "Average", "Grade"),
                    show="headings")

tree.heading("Name", text="Name")
tree.heading("Total", text="Total")
tree.heading("Average", text="Average")
tree.heading("Grade", text="Grade")

tree.pack(pady=20, fill="both", expand=True)

# Stats labels
topper_label = tk.Label(root, text="🥇 Topper:",
                        bg="#1e1e2f", fg="#00ff00",
                        font=("Arial", 14, "bold"))
topper_label.pack()

lowest_label = tk.Label(root, text="⚠️ Lowest:",
                        bg="#1e1e2f", fg="#ff4d4d",
                        font=("Arial", 14, "bold"))
lowest_label.pack()

root.mainloop()