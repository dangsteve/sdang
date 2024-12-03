import pandas as pd

transactions = []  # A list to hold transactions
balance = 0        # Initialize balance

# Function to add income
def add_income():
    global balance  
    try:
        amount = float(input("Enter the amount of income: "))
        description = input("Enter a description for this income (optional): ")
        transaction = {
            "amount": amount,
            "type": "income",
            "description": description
        }
        transactions.append(transaction)
        balance += amount  # Increase the balance by the income amount
        print(f"Income of ${amount} added.")
    except ValueError:
        print("Invalid input. Please enter a numeric value for income.")

# Function to add expense
def add_expense():
    global balance
    try:
        amount = float(input("Enter the amount of expense: "))
        description = input("Enter a description for this expense (optional): ")
        transaction = {
            "amount": amount,
            "type": "expense",
            "description": description
        }
        transactions.append(transaction)
        balance -= amount  # Decrease the balance by the expense amount
        print(f"Expense of ${amount} added.")
    except ValueError:
        print("Invalid input. Please enter a numeric value for expense.")

# Function to view transactions
def view_transactions(transactions):
    if transactions:
        for i, transaction in enumerate(transactions, start=1):
            print(f"{i}. {transaction['type'].capitalize()} of ${transaction['amount']:.2f} - {transaction['description']}")
    else:
        print("No transactions to show.")

# Function to save transactions to Excel
def save_to_excel(transactions):
    df = pd.DataFrame(transactions)
    df.to_excel('transactions.xlsx', index=False, engine='openpyxl')
    print("Transactions saved to 'transactions.xlsx'")

# Main function
def main():
    while True:
        print("\n1. Add Income")
        print("2. Add Expense")
        print("3. View Balance")
        print("4. View Transactions")
        print("5. Save to Excel")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_income()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            print(f"Current Balance: ${balance:.2f}")
        elif choice == "4":
            view_transactions(transactions)
        elif choice == "5":
            save_choice = input("Do you want to save transactions to Excel? (y/n): ")
            if save_choice.lower() == "y":
                save_to_excel(transactions)
        elif choice == "6":
            break
        else:
            print("Invalid option. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
