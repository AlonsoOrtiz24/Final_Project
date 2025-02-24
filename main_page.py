from Program_Functions.add_and_remove import new_expense, remove_expense
from Program_Functions.Saving_and_loading import save_expenses, load_expenses
from Program_Functions.viewing_expenses import view_expenses
# Load existing expenses at the start
load_expenses()

while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Remove Expense")
    print("4. Save and Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        new_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        remove_expense()
    elif choice == "4":
        save_expenses()
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1-4.")