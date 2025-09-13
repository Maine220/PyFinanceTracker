class Transaction:
    def __init__(self, date, category, amount, t_type):
        self.date = date
        self.category = category
        self.amount = amount
        self.type = t_type  # "income" or "expense"

    def to_dict(self):
        return {
            "date": self.date,
            "category": self.category,
            "amount": self.amount,
            "t_type": self.type
        }

class FinanceTracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def summary(self):
        income = sum(t.amount for t in self.transactions if t.type == "income")
        expenses = sum(t.amount for t in self.transactions if t.type == "expense")
        print(f"Total Income: ${income:.2f}")
        print(f"Total Expenses: ${expenses:.2f}")
        print(f"Net Savings: ${income - expenses:.2f}")

    def category_summary(self):
        summary = {}
        for t in self.transactions:
            if t.type == "expense":
                summary[t.category] = summary.get(t.category, 0) + t.amount
        print("Expenses by Category:")
        for cat, amt in summary.items():
            print(f"{cat}: ${amt:.2f}")
