import matplotlib.pyplot as plt
from calculations import expense_by_category
from calculations import monthly_expense_summary
import pandas as pd
from operations import load_data


def show_category_chart():

    data = load_data()

    # Convert LIST → DataFrame ✅
    data = pd.DataFrame(data)

    if data.empty:
        print("No data available")
        return

    # Category wise total
    category_total = data.groupby("category")["amount"].sum()

    # Plot
    category_total.plot(kind="bar")

    plt.title("Category Wise Expenses")
    plt.xlabel("Category")
    plt.ylabel("Amount")

    plt.show()    
    

def show_monthly_trend():

    
    data = load_data()

    # Convert list → DataFrame
    data = pd.DataFrame(data)

    if data.empty:
        print("No data available")
        return

    # Convert date column to datetime
    data["date"] = pd.to_datetime(data["date"])

    # Extract month
    data["month"] = data["date"].dt.to_period("M")

    # Monthly total expense
    monthly_total = data.groupby("month")["amount"].sum()

    # Plot line chart
    monthly_total.plot(kind="line", marker="o")

    plt.title("Monthly Expense Trend")
    plt.xlabel("Month")
    plt.ylabel("Total Amount")

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show() 
    
