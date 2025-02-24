def remove_expense():
    """
    Removes an expense from a selected category.
    :return:
    """
    category = input("Enter category to remove an expense from (Food, Transport, Entertainment, Others): ").strip()
    if category not in expenses or not expenses[category]:
        print("Invalid category or no expenses recorded in this category.")
        return

    print(f"\nExpenses in {category}:")
    for i, (amount, date) in enumerate(expenses[category]):
        print(f"{i + 1}. ${amount:.2f} on {date}")

    try:
        index = int(input("Enter the number of the expense to remove: ")) - 1
        if 0 <= index < len(expenses[category]):
            removed_expense = expenses[category].pop(index)
            print(f"Removed ${removed_expense[0]:.2f} on {removed_expense[1]}.")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")