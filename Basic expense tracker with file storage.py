import csv
import os

FILENAME = "expenses.csv"

# CSV file ke liye headers
HEADERS = ["Type", "Amount", "Description"]

# Agar file exist nahi karti to create karenge
if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(HEADERS)

# Function to add record
def add_record(record_type, amount, description):
    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([record_type, amount, description])
    print("✅ Record added successfully!\n")

# Function to show summary
def show_summary():
    total_income = 0
    total_expense = 0

    with open(FILENAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            amount = float(row["Amount"])
            if row["Type"] == "Income":
                total_income += amount
            elif row["Type"] == "Expense":
                total_expense += amount

    net_balance = total_income - total_expense

    print("\n📊 Summary:")
    print(f"Total Income:  ₹{total_income}")
    print(f"Total Expense: ₹{total_expense}")
    print(f"Net Balance:   ₹{net_balance}\n")

# Main Program
def main():
    while True:
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Show Summary")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            amount = float(input("Enter income amount: "))
            desc = input("Enter description: ")
            add_record("Income", amount, desc)

        elif choice == "2":
            amount = float(input("Enter expense amount: "))
            desc = input("Enter description: ")
            add_record("Expense", amount, desc)

        elif choice == "3":
            show_summary()

        elif choice == "4":
            print("👋 Exiting... Data saved in expenses.csv")
            break

        else:
            print("❌ Invalid choice, try again.\n")

if __name__ == "__main__":
    main()