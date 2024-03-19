import json
import os

# Function to load transactions from file
def load_transactions():
    if os.path.exists("transactions.json"):
        with open("transactions.json", "r") as file:
            return json.load(file)
    else:
        return {"income": [], "expenses": []}

# Function to save transactions to file
def save_transactions(transactions):
    with open("transactions.json", "w") as file:
        json.dump(transactions, file, indent=4)

# Function to display transactions
def display_transactions(transactions):
    print("\nIncome:")
    for income in transactions["income"]:
        print(f"{income['category']}: ${income['amount']}")
    print("\nExpenses:")
    for expense in transactions["expenses"]:
        print(f"{expense['category']}: ${expense['amount']}")

# Function to add an income transaction
def add_income(transactions):
    category = input("Enter income category: ")
    amount = float(input("Enter income amount: "))
    transactions["income"].append({"category": category, "amount": amount})
    save_transactions(transactions)
    print("Income added successfully!")

# Function to add an expense transaction
def add_expense(transactions):
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    transactions["expenses"].append({"category": category, "amount": amount})
    save_transactions(transactions)
    print("Expense added successfully!")

# Function to calculate remaining budget
def calculate_budget(transactions):
    total_income = sum(income["amount"] for income in transactions["income"])
    total_expenses = sum(expense["amount"] for expense in transactions["expenses"])
    remaining_budget = total_income - total_expenses
    return remaining_budget

# Function to display expense analysis
def expense_analysis(transactions):
    categories = {}
    for expense in transactions["expenses"]:
        category = expense["category"]
        amount = expense["amount"]
        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount
    print("\nExpense Analysis:")
    for category, amount in categories.items():
        print(f"{category}: ${amount}")

# Main function
def main():
    transactions = load_transactions()
    while True:
        print("\nMenu:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Display Transactions")
        print("4. Calculate Remaining Budget")
        print("5. Expense Analysis")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_income(transactions)
        elif choice == "2":
            add_expense(transactions)
        elif choice == "3":
            display_transactions(transactions)
        elif choice == "4":
            remaining_budget = calculate_budget(transactions)
            print(f"\nRemaining Budget: ${remaining_budget}")
        elif choice == "5":
            expense_analysis(transactions)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

    print("Thank you for using the Personal Budget Tracker!")

if _name_ == "_main_":
    main()