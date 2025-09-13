# PyFinanceTracker

A Python command-line tool to track personal income, expenses, and budgets.

## Features
- Add income or expense transactions with date and category.
- View overall income, expenses, and net savings.
- View expenses by category.
- Stores transactions in a JSON file (data/transactions.json)
- Robust handling of empty or corrupted JSON files

## Installation
1. Clone the repo:

bash:
git clone https://github.com/maine220/PyFinanceTracker.git

2. Make sure you have Python 3 installed:

python3 --version

## Usage
bash:
python3 main.py

You will see a menu:

1. Add Transaction
2. Show Summary
3. Show Category Summary
4. Exit

Add Transaction: Input date, category, amount, and type (income or expense).

Show Summary: See total income, total expenses, and net savings.

Show Category Summary: View total expenses per category.

Exit: Close the program.

##Technologies Used

- Python 3
- JSON for data storage
- Object-Oriented Programming (OOP)
- Command-Line Interface (CLI)
