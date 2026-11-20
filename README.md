# Personal Expense Tracker

A command-line Expense Tracker built using Python. It allows users to manage daily expenses, generate reports, and track monthly budgets. Data is stored locally using JSON files.

## Features

- Add, view, update, and delete expenses
- Calculate total expenses
- Generate category-wise expense summaries
- Search expenses
- Filter expenses by date
- Generate monthly and yearly reports
- Set and update monthly budgets
- Calculate remaining budget and detect overspending
- Store expenses and budgets using JSON for data persistence

## Technologies Used

- Python
- JSON
- Decimal
- Datetime

## Project Structure

```text
Expense_Tracker/
│
├── main.py
├── expense.py
├── expenses.json
├── budgets.json
└── README.md
```

## How to Run

1. Install Python.
2. Clone or download this repository.
3. Open the project folder in the terminal.
4. Run:

```bash
python main.py
```

## Data Storage

The application stores expense records in `expenses.json` and monthly budget information in `budgets.json`. Data remains available after restarting the application.

## Purpose

This project was developed to practise Python programming, functions, object-oriented programming, exception handling, file handling, JSON, and data management.