import csv
from expense import Expense

FILE_PATH = "data/expenses.csv"

def load_expenses():
    expenses = []
    try:
        with open(FILE_PATH, "r") as f:
            reader = csv.DictReader(f)
            for r in reader:
                expenses.append(Expense(r["Amount"], r["Category"], r["Date"], r["Description"]))
    except FileNotFoundError:
        pass
    return expenses

def save_expenses(expenses):
    with open(FILE_PATH, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Date","Category","Amount","Description"])
        for e in expenses:
            writer.writerow([e.date,e.category,e.amount,e.description])
