from add_and_remove import expenses

def save_expenses():
    """
    Saves expenses to a file (expenses.txt)
    :return:
    """
    with open("expenses.txt", "w") as file:
        for category, transactions in expenses.items():
            for amount, date in transactions:
                file.write(f"{category},{amount},{date}\n")  # Save category, amount, and date
    print("Expenses saved successfully!")

def load_expenses():
    """
    Load the expenses previously recorded from the file (expenses.txt)
    :return:
    """
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                category, amount, date = line.strip().split(",")  # Read "Category,Amount,Date"
                if category in expenses:
                    expenses[category].append((float(amount), date))  # Convert amount to float
    except FileNotFoundError:
        print("No saved expenses found.")