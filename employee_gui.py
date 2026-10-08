import tkinter as tk
from tkinter import messagebox
import mysql.connector


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vishesh@123",
    database="employee_db"
)

cursor = db.cursor()

root = tk.Tk()
root.title("Employee Management System")
root.geometry("600x400")

def promote_employee():

    employee_id = input("Enter Employee ID to promote: ")
    new_designation = input("Enter new designation: ")
    new_salary = input("Enter new salary: ")

    cursor.execute(
        "UPDATE employees SET designation=%s, salary=%s WHERE id=%s",
        (new_designation, new_salary, employee_id)
    )

    db.commit()

    print("Employee promoted successfully")


def remove_employee():

    employee_id = input("Enter Employee ID to remove: ")

    cursor.execute(
        "DELETE FROM employees WHERE id = %s",
        (employee_id,)
    )

    db.commit()

    print("Employee removed successfully")


def add_employee():

    form = tk.Toplevel(root)
    form.title("Add Employee")
    form.geometry("400x400")

    tk.Label(form, text="Name").pack()
    name = tk.Entry(form)
    name.pack()

    tk.Label(form, text="Email").pack()
    email = tk.Entry(form)
    email.pack()

    tk.Label(form, text="Department").pack()
    department = tk.Entry(form)
    department.pack()

    tk.Label(form, text="Designation").pack()
    designation = tk.Entry(form)
    designation.pack()

    tk.Label(form, text="Salary").pack()
    salary = tk.Entry(form)
    salary.pack()

    def save_employee():

        cursor.execute(
            "INSERT INTO employees "
            "(name, email, department, designation, salary) "
            "VALUES (%s, %s, %s, %s, %s)",
            (
                name.get(),
                email.get(),
                department.get(),
                designation.get(),
                salary.get()
            )
        )

        db.commit()

        print("Employee added successfully")

        form.destroy()

    tk.Button(
        form,
        text="Save Employee",
        command=save_employee
    ).pack(pady=20)


tk.Button(
    root,
    text="Add Employee",
    width=20,
    command=add_employee
).pack(pady=10)

tk.Button(
    root,
    text="Remove Employee",
    width=20,
    command=remove_employee
).pack(pady=10)

tk.Button(
    root,
    text="Promote Employee",
    width=20,
    command=promote_employee
).pack(pady=10)

def display_employees():
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()

    if not employees:
        messagebox.showinfo("Employees", "No employees found")
        return

    data = ""

    for employee in employees:
        data += f"ID: {employee[0]}\n"
        data += f"Name: {employee[1]}\n"
        data += f"Email: {employee[2]}\n"
        data += f"Department: {employee[3]}\n"
        data += f"Designation: {employee[4]}\n"
        data += f"Salary: {employee[5]}\n"
        data += "-" * 30 + "\n"

    messagebox.showinfo("Employees", data)
tk.Button(
    root,
    text="Display Employees",
    width=20,
    command=display_employees
).pack(pady=10)



root.mainloop()