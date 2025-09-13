import json
from finance_tracker.tracker import Transaction

FILE_PATH = "data/transactions.json"

def save_transactions(transactions):
    with open(FILE_PATH, 'w') as f:
        json.dump([t.to_dict() for t in transactions], f, indent=4)

def load_transactions():
    try:
        with open(FILE_PATH, 'r') as f:
            content = f.read().strip()
            if not content:
                return []
            data = json.loads(content)
            transactions = []
            for t in data:
                if "t_type" not in t and "type" in t:
                    t["t_type"] = t.pop("type")
                transactions.append(Transaction(**t))
            return transactions
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Warning: JSON file is corrupted. Starting with empty list.")
        return []




