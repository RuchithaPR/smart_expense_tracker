import pandas as pd
from database import connect_db


def load_data():
    conn = connect_db()
    mydata = pd.read_sql_query("SELECT * FROM transactions", conn)
    conn.close()
    return mydata

def get_total_income():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(amount) FROM transactions WHERE type='income'")
    result = cursor.fetchone() #fetchone() returns a tuple like (5000.0,)

    conn.close()

    return result[0] if result[0] else 0

def get_total_expense():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(amount) FROM transactions WHERE type='expense'")
    result = cursor.fetchone()

    conn.close()

    return result[0] if result[0] else 0

def get_balance():
    return get_total_income() - get_total_expense()

#category wise expense total
def expense_by_category():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT category, SUM(amount)
        FROM transactions
        WHERE type='expense'
        GROUP BY category
    """)

    rows = cursor.fetchall()
    conn.close()
    return rows


#monthly expense summary
def monthly_expense_summary():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT strftime('%Y-%m', date) AS month,
               SUM(amount)
        FROM transactions
        WHERE type='expense'
        GROUP BY month
        ORDER BY month
    """)

    rows = cursor.fetchall()
    conn.close()
    return rows

def highest_expense_category():
    df = load_data()

    # take only expenses
    expense_df = df[df["type"] == "expense"]

    # category total
    category_total = expense_df.groupby("category")["amount"].sum()

    # highest category
    highest = category_total.idxmax()
    amount = category_total.max()

    return highest, amount


    

