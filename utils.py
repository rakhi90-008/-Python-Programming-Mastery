from datetime import datetime

def validate_amount(value):
    amount = float(value)
    if amount <= 0:
        raise ValueError("Amount must be positive")
    return amount

def validate_date(date_str):
    datetime.strptime(date_str, "%Y-%m-%d")
    return date_str

def validate_category(category):
    allowed = ["Food","Transport","Entertainment","Shopping","Other"]
    if category not in allowed:
        raise ValueError("Invalid category")
    return category
