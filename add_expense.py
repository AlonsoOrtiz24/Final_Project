expenses = {
    "Food":[],
    "Transport":[],
    "Entertainment":[],
    "Other":[],
}

def new_expense():
    """
    Function that asks the user to enter an expense, which will be added to a list
    :return:
    """
    category = input("Enter a category (Food, Transport, Entertainment, Others): ").strip()
    if category not in expenses:
        print("Invalid Category introduced. Please try again")
        return

    try:
        amount = float(input("Enter the exact amount spend: "))
        date = input("Enter date (DD-MM)").strip()

        expenses[category].append((amount,date))
        print(f"{amount} spent on {category} on {date}")
    except ValueError:
        print("Invalid amount. Try again!")