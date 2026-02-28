from database import connect_db
import json

def insert_user(name,email):
    try:
        conn=connect_db()
        cursor=conn.cursor()
    
        cursor.execute(
        "INSERT INTO users (name,email) VALUES (?,?)",(name,email)
        )
    
        conn.commit()
    
    except Exception as e:
        print("Insert user Error:",e)
    finally:
        conn.close()
        
def insert_transaction(user_id, amount, type, category, date):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO transactions (user_id, amount, type, category, date)
        VALUES (?, ?, ?, ?, ?)
    """, (user_id, amount, type, category, date))
        conn.commit()
    
    except Exception as e:
        print("Transaction Error:",e)
        conn.close()
        
def update_transaction(transaction_id, new_amount):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE transactions
        SET amount = ?
        WHERE id = ?
    """, (new_amount, transaction_id))

    conn.commit()
    conn.close()


def delete_transaction(transaction_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM transactions
        WHERE id = ?
    """, (transaction_id,))

    conn.commit()
    conn.close()
    

def load_data():

    import json

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
        return data

    except Exception as e:
        print("Error loading data:", e)
        return []



def show_transactions():
    conn=connect_db()
    cursor=conn.cursor()
    
    cursor.execute("SELECT * FROM transactions")
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)
        
        conn.close()
        
        
def export_to_json():

    import json
    from database import connect_db

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM transactions")
    rows = cursor.fetchall()

    data = []

    for row in rows:
        data.append({
            "id": row[0],
            "user_id": row[1],
            "amount": row[2],
            "type": row[3],
            "category": row[4],
            "date": row[5]
        })

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

    conn.close()
