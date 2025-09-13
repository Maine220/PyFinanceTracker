from finance_tracker.tracker import FinanceTracker, Transaction
from finance_tracker.storage import save_transactions, load_transactions

tracker = FinanceTracker()
tracker.transactions = load_transactions()

def main():
    while True:
        print("\n1. Add Transaction")
        print("2. Show Summary")
        print("3. Show Category Summary")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            date = input("Date (YYYY-MM-DD): ")
            category = input("Category: ")
            try:
                amount = float(input("Amount: "))
            except ValueError:
                print("Amount must be a number!")
                continue
            t_type = input("Type (income/expense): ").lower()
            if t_type not in ["income", "expense"]:
                print("Type must be 'income' or 'expense'")
                continue
            tracker.add_transaction(Transaction(date, category, amount, t_type))
            save_transactions(tracker.transactions)
            print("Transaction added!")
        elif choice == '2':
            tracker.summary()
        elif choice == '3':
            tracker.category_summary()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
