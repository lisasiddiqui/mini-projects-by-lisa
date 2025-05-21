import os

def add_expense():
    category = input("Enter category (e.g., Food, Transport): ").strip()
    amount = input("Enter amount spent: ").strip()
    
    
    try:
        amount = float(amount)
    except ValueError:
        print("Invalid amount! Please enter a number.")
        return
    
    
    with open("expenses.txt", "a") as file:
        file.write(f"{category},{amount}\n")
    print("Expense added successfully.\n")

def view_expenses():
    if not os.path.exists("expenses.txt"):
        print("No expenses recorded yet.\n")
        return
    
    expenses = {}
    total = 0.0
    
    
    with open("expenses.txt", "r") as file:
        for line in file:
            line = line.strip()
            if line:
                category, amount = line.split(",")
                amount = float(amount)
                expenses[category] = expenses.get(category, 0) + amount
                total += amount
    
    
    print("\nExpense Summary:")
    for category, amount in expenses.items():
        print(f" - {category}: ₹{amount:.2f}")
    print(f"Total Spent: ₹{total:.2f}\n")

def main():
    print("Welcome to the Expense Tracker CLI!\n")
    
    while True:
        print("Choose an option:")
        print("1. Add an expense")
        print("2. View expenses summary")
        print("3. Exit")
        
        choice = input("Your choice: ").strip()
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Goodbye! Stay financially wise 😊")
            break
        else:
            print("Invalid choice, try again.\n")

if __name__ == "__main__":
    main()
