from Program_Functions.add_and_remove import expenses
def view_expenses():
    """
    Displays all recorded expenses with dates
    :return:
    """
    print("\nExpense Summary:")

    total_spending = 0
    for category, transactions in expenses.items():
        print(f"\n{category}:")

        if not transactions:
            print("No expenses recorded.")
        else:
            for amount, date in transactions:
                print(f"  - ${amount:.2f} on {date}")  # Shows amount and date
                total_spending += amount
    print(f"\nTotal Spending: ${total_spending:.2f}")
