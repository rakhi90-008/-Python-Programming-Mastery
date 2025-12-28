from collections import defaultdict

def category_summary(expenses):
    s = defaultdict(float)
    for e in expenses:
        s[e.category] += e.amount
    return s

def monthly_report(expenses, month):
    return sum(e.amount for e in expenses if e.date.startswith(month))
