import json
from expense import Expense
from decimal import Decimal, InvalidOperation
from datetime import datetime
def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            expense_data = json.load(file)
        return [
            Expense(
                Decimal(item["amount"]),
                item["category"],
                item["description"],
                item.get("date")
            )
            for item in expense_data
        ]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Warning: expenses.json was corrupted or empty. Starting with an empty list.")
        return []
def save_expenses(expenses):
    expenses_data = [expense.to_dict() for expense in expenses]
    with open("expenses.json", "w") as file:
        json.dump(expenses_data,file, indent= 4)

expenses = load_expenses()

def add_expense(expenses):
    while True:
        try:
            amount = Decimal(input("Enter amount: ").strip())
            if amount <= 0:
                print("Enter a positive amount")
            else:
                break
        except ValueError:
            print("Enter a valid input")
    while True:
        category = input("Enter category: ").strip()

        if not category:
            print("Category cannot be empty")
        else:
            break
    while True:
        description = input("Enter description: ").strip()

        if not description:
            print("Description cannot be empty")
        else:
            break
    while True:
        try:
            date_input = input("Enter the date in (YYYY-MM-DD):")
            date = datetime.strptime(date_input, "%Y-%m-%d").date()
            date = date.strftime("%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date. Try again.")

            
        
    new_expense = Expense(amount,category,description,date)
    expenses.append(new_expense)
    print("New expense was added")
    save_expenses(expenses)


def delete_expense(expenses):
    if not expenses:
        print("No expenses available to delete")
        return expenses
    while True:
        try:
            choice = int(input("Enter delete expense number: "))
            if choice <= 0:
                print("Enter a positive value")
            elif choice > len(expenses):
                print("No expenses available to delete")
            else:
                break
        except ValueError:
            print("Enter valid input")
    expenses.pop(choice - 1)
    save_expenses(expenses)
    print("Expense deleted successfully.")

def update(expenses):
    if not expenses:
        print("No expenses available to update")
        return expenses
    print("What do you want to update?\n")
    select_update = ["Amount", "Category", "Description", "Cancel"]

    while True:
        a = 0
        while a < len(select_update):
            print(f"{a+1}. {select_update[a]}" )
            a += 1
        try:
                choice_num = int(input("Select a number: "))
        
                if choice_num == 4:
                    print("Canceled the update")
                    return
                elif 1 <= choice_num < 4:
                    if choice_num ==1:
                        while True:
                            try:
                                choice = int(input("Enter update expense number: "))
                                if choice <=0:
                                    print("Enter a positive value")
                                elif choice > len(expenses):
                                    print("No expenses available to update")
                                else:
                                    break
                            except  ValueError:
                                print("Enter valid input")
                        selected = expenses[choice - 1]
                        while True:
                            try:    
                                new_amount = Decimal(input("Enter new amount: "))
                                if new_amount <= 0:
                                    print("Enter a positive amount")
                                else:
                                    break
                            except ValueError:
                                print("Enter a valid input")
                        selected.amount = new_amount
                        save_expenses(expenses)
                        print("Expense updated successfully.")
                        return expenses
                    elif choice_num == 2:
                        while True:
                            try:
                                choice = int(input("Enter update expense number: "))
                                if choice <=0:
                                    print("Enter a positive value")
                                elif choice > len(expenses):
                                    print("No expenses available to update")
                                else:
                                    break
                            except ValueError:
                                print("Enter valid input")
                        selected = expenses[choice-1]
                        while True :
                            new_category = input("Enter new category: ").strip()
                            if not new_category:
                                print("Category should not be empty")
                
                            else:
                                break
                        selected.category = new_category
                        save_expenses(expenses)
                        print("Expense category updated successfully.")
                        return expenses
                    elif choice_num == 3:
                        while True:
                            try:
                                choice = int(input("Enter update expense number: "))
                                if choice <=0:
                                    print("Enter a positive value")
                                elif choice > len(expenses):
                                    print("No expenses available to update")
                                else:
                                    break
                            except ValueError:
                                print("Enter valid input")
                        selected = expenses[choice-1]
                        while True:
                            new_description = input("Enter new description: ").strip()
                            if not new_description:
                                print("Discription should not be empty")
                            else:
                                break
                        selected.description = new_description
                        save_expenses(expenses)
                        print("Expense description updated successfully.")
                        return expenses

                else:
                    print("Invalid choice. Please select 1-4")
        except ValueError:
            print("Enter valid number\n")


def calculate_total(expenses):
    total = 0
    for add in expenses:
        total += add.amount
    return total

def category_summary(expenses):
    summary = {}
    for same in expenses:
        category = same.category
        amount = same.amount
        if category in summary:
            summary[category] = summary[category] + amount
        else:
            summary[category] = amount
    return summary

def search_expenses(expenses):
    if not expenses:
        print("No expenses available to search")
        return expenses
    else:
        print("Enter category to search: ")
    search = input()
    count = 0
    count_amount = 0
    for expense in expenses:
        if search == expense.category:
            count_amount += expense.amount
            count += 1
            print(expense)
    if count == 0:
        print("no matching expenses found")
    else:
        print(f"Total expenses: {count}")
        print(f"Total amount for {search} : {count_amount}")

def filter_by_date(expenses):
    if not expenses:
        print("No expenses available to date")
        return expenses
    else:
        print("Enter date to search(YYYY-MM-DD): ")
    while True:
        try:
            date = input()
            date = datetime.strptime(date, "%Y-%m-%d").date()
            date = date.strftime("%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date. Try again.")
    count = 0
    count_amount = 0
    for expense in expenses:
        if date == expense.date:
            count_amount += expense.amount
            count += 1
            print(expense)
    if count == 0:
        print("No date found")
    else:
        print(f"Total expenses: {count}")
        print(f"Total expences on {date} : ₹{count_amount}")


def load_budgets():
    try:
        with open("budgets.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_budgets(budgets):
    with open("budgets.json", "w") as file:
        json.dump(budgets, file, indent = 4)

def set_monthly_budget(date):
    budgets = load_budgets()

    if date in budgets:
        print(f"Existing budget: ₹{budgets[date]}")

        choice = input("Do you want to update this budget? (yes/no): ").lower()

        if choice == "yes":
            while True:
                try:
                    budget = Decimal(input("Enter new monthly budget: "))

                    if budget <= 0:
                        print("Budget must be greater than zero.")
                    else:
                        budgets[date] = float(budget)
                        save_budgets(budgets)
                        print("Budget updated successfully!")
                        return budget

                except (ValueError, InvalidOperation):
                    print("Enter a valid amount.")

        return Decimal(str(budgets[date]))

    while True:
        try:
            budget = Decimal(input("Enter your monthly budget: "))

            if budget <= 0:
                print("Budget must be greater than zero.")
            else:
                budgets[date] = float(budget)
                save_budgets(budgets)
                return budget

        except (ValueError, InvalidOperation):
            print("Enter a valid amount.")

def expense_report(expenses, report_type):
    count = 0
    count_amount = 0
    filtered_expenses = []

    if not expenses:
        print("No expenses available to date")
        return expenses

    while True:
        if report_type == "monthly":
            print("Enter year and month to search(YYYY-MM):")
            try:
                date = input()
                date = datetime.strptime(date, "%Y-%m").date()
                date = date.strftime("%Y-%m")
                break
            except ValueError:
                print("Invalid date. Try again.")
        elif report_type == "yearly":
            print("Enter year to search(YYYY):")
            try:
                date = input()
                date = datetime.strptime(date, "%Y").date()
                date = date.strftime("%Y")
                break
            except ValueError:
                print("Invalid date. Try again.")
    for expense in expenses:
        if report_type == "monthly" and date == expense.date[:7]:
            filtered_expenses.append(expense)
            count_amount += expense.amount
            count += 1
            print(expense)
        elif report_type == "yearly" and date == expense.date[:4]:
            filtered_expenses.append(expense)
            count_amount += expense.amount
            count += 1
            print(expense)
    if count == 0:
        print("No date found")
    else:
        summary = category_summary(filtered_expenses)

        for category, amount in summary.items():
            print(f"{category} : ₹{amount}")
        print(f"Total expenses: {count}")
        print(f"Total expenses on {date} : ₹{count_amount}")
        if report_type == "monthly":
            budget = set_monthly_budget(date)
            remaining = budget - count_amount

            if remaining >= 0:
                print(f"remaining budget: ₹{remaining}")
            else:
                print(f"Budget exceeded by: ₹{abs(remaining)}")





expense_tracker = [
    "Add Expense" ,
    "View Expenses" ,
    "Calculate Total",
    "Category Summary",
    "Delete Expense",
    "Update Expense",
    "Search Expence",
    "Filter Expenses by Date",
    "Filter by year and month",
    "Filter by year",
    "Exit"
    ]

while True:
    i = 0

    while i < len(expense_tracker):    
        print(f"{i+1}. {expense_tracker[i]}")
        i += 1
    try:
        choice_num = int(input("Select a number: "))

        if choice_num == 11:
            print("Exiting Expense Tracker...")
            break
        elif 1 <= choice_num < 11:
            if choice_num ==1:
                add_expense(expenses)
            elif choice_num == 2:
                if not expenses:
                    print("No expenses found.")
                else:
                    for i, expense in enumerate(expenses, start=1):
                        print(f"{i}. {expense.date} | {expense.category} | ₹{expense.amount} | {expense.description}")
            elif choice_num == 3:
                total = calculate_total(expenses)
                print(f"Total expenses:₹{total}")
            elif choice_num == 4:
                if not expenses:
                    print("No expenses found.")
                else:
                    summary = category_summary(expenses)
                    for category, amount in summary.items():
                        print(f"{category} , ₹{amount}")
            elif choice_num == 5:
                delete_expense(expenses)
            elif choice_num == 6:
                update(expenses)
            elif choice_num ==7:
                search_expenses(expenses)
            elif choice_num ==8:
                filter_by_date(expenses)
            elif choice_num == 9:
                expense_report(expenses, "monthly")
            elif choice_num ==10:
                expense_report(expenses, "yearly")
        else:
            print("Invalid input.\n")
    except ValueError:
        print("Enter valid number\n")