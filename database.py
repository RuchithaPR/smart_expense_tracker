import sqlite3
import pandas as pd



def connect_db():
    conn=sqlite3.connect("expenses.db")
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def create_tables():
    conn=connect_db()
    cursor=conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT
    )
    """)
    
    cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS transactions(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    amount REAL NOT NULL,
    type TEXT NOT NULL,
    category TEXT NOT NULL,
    date TEXT NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)
    
    cursor.execute("""
    CREATE INDEX IF NOT EXISTS idx_date
    ON transactions(date);
    """)    
    
    cursor.execute("""
    CREATE INDEX IF NOT EXISTS idx_category
    ON transactions(category);
    """)    
    
    conn.commit()
    conn.close()
    



    
    
    
   
      

       
    

    





