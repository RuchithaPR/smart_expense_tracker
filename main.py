import matplotlib.pyplot as plt
from operations import (
    insert_user,
    insert_transaction,
    show_transactions,
    update_transaction,
    delete_transaction,
    export_to_json

)
from database import *
from calculations import *
from visualizations import *



create_tables()

def insert_default_user():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT OR IGNORE INTO users (id, name, email)
    VALUES (1, 'Ruchitha', 'ruchitha@gmail.com')
    """)

    conn.commit()
    conn.close()



insert_default_user()

while True:
    print("\n1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. Update Transaction")
    print("5. Delete Transaction")
    print("6. show category chart")
    print("7. show monthly trend")
    print("8. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        user_id = 1
        
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        date = input("Enter date (YYYY-MM-DD): ")
        
        insert_transaction(user_id, amount, "income", category, date)
        
        export_to_json()
        
        print("Transaction Added Successfully!")        
        
        

        if amount <= 0:
            print("Invalid amount.")
        else:
            insert_transaction(1, amount, "income", category, date)

    elif choice == "2":
        user_id = 1
        amount = float(input("Enter expense amount: "))
        category = input("Enter category: ")
        date = input("Enter date (YYYY-MM-DD): ")
        insert_transaction(user_id, amount, "expense", category, date)
        export_to_json()        

        if amount <= 0:
            print("Invalid amount.")
        else:
            insert_transaction(1, amount, "expense", category, date)

    elif choice == "3":
        show_transactions()

    elif choice == "4":
        transaction_id = int(input("Enter transaction ID to update: "))
        new_amount = float(input("Enter new amount: "))
        update_transaction(transaction_id, new_amount)

    elif choice == "5":
        transaction_id = int(input("Enter transaction ID to delete: "))
        delete_transaction(transaction_id)
        
    elif choice == "6":
        show_category_chart() #not using print because chart functions display, not return values
        break
    
    elif choice == "7":
        show_monthly_trend()
        break    

    elif choice == "8":
        print("Exiting program.")
        break

    else:
        print("Invalid choice.")


    conn = connect_db()
    cursor = conn.cursor()
        
    cursor.execute("SELECT * FROM users")
    print("USERS TABLE DATA:", cursor.fetchall())
        
    conn.close()





