# Smart Expense Tracker

A CLI-based Smart Expense Tracker built using Python, SQLite, and Pandas.  
This project helps users record daily expenses, store them in a database, and analyze spending patterns.

## Features

- Add and manage daily expenses
- Store expense data using SQLite database
- Perform calculations on expenses
- Visualize spending data
- Command Line Interface (CLI)

## Technologies Used

- Python
- SQLite
- Pandas
- Matplotlib

## Project Structure

smart_expense_tracker/

main.py → Main program entry point  
database.py → Database connection and queries  
operations.py → Expense operations  
calculations.py → Expense calculations  
visualizations.py → Graphs and charts  
data.json → Sample data  
expenses.db → SQLite database

## How to Run

1. Clone the repository

git clone https://github.com/RuchithaPR/smart_expense_tracker.git

2. Go to the project folder

cd smart_expense_tracker

3. Install dependencies

pip install pandas matplotlib

4. Run the project

python main.py

## Visualizations

### Expense Distribution
![category_wise_expenses_SET](expense_chart.png)

### Monthly Spending
![monthly_expense_trend_SET](monthly_spending.png)

## Future Improvements

- Add GUI interface
- Add expense category prediction
- Monthly expense reports
- Export reports to Excel

## Author

Ruchitha P R
