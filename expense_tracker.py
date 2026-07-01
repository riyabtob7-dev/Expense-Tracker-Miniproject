import tkinter as tk
from tkinter import messagebox

expenses = []

# Load expenses from file
try:
    with open("expenses.txt", "r") as file:
        for line in file:
            name, amount = line.strip().split(",")
            expenses.append([name, float(amount)])
except FileNotFoundError:
    pass


def add_expense():
    name = name_entry.get()
    amount = amount_entry.get()

    if name == "" or amount == "":
        messagebox.showerror("Error", "Please fill all fields.")
        return

    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Error", "Amount must be a number.")
        return

    expenses.append([name, amount])

    with open("expenses.txt", "a") as file:
        file.write(f"{name},{amount}\n")

    messagebox.showinfo("Success", "Expense Added Successfully!")

    name_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)


def view_expenses():
    expense_list.delete(0, tk.END)

    if len(expenses) == 0:
        expense_list.insert(tk.END, "No Expenses Found")
    else:
        for expense in expenses:
            expense_list.insert(
                tk.END,
                f"{expense[0]} - ₹{expense[1]}"
            )


def total_spending():
    total = sum(expense[1] for expense in expenses)
    messagebox.showinfo("Total Spending", f"₹ {total}")


# Window
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("500x500")

# Heading
title = tk.Label(
    root,
    text="Expense Tracker",
    font=("Arial", 20, "bold")
)
title.pack(pady=10)

# Expense Name
tk.Label(root, text="Expense Name").pack()

name_entry = tk.Entry(root, width=35)
name_entry.pack()

# Amount
tk.Label(root, text="Amount").pack()

amount_entry = tk.Entry(root, width=35)
amount_entry.pack(pady=5)

# Buttons
tk.Button(
    root,
    text="Add Expense",
    width=20,
    command=add_expense
).pack(pady=5)

tk.Button(
    root,
    text="View Expenses",
    width=20,
    command=view_expenses
).pack(pady=5)

tk.Button(
    root,
    text="Show Total",
    width=20,
    command=total_spending
).pack(pady=5)

# Listbox
expense_list = tk.Listbox(root, width=50, height=12)
expense_list.pack(pady=15)

root.mainloop()