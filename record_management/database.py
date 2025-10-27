# database.py
import sqlite3

DB_NAME = "records.db"

def connect_db():
    return sqlite3.connect(DB_NAME)

def create_table():
    with connect_db() as conn:
        with open("schema.sql", "r") as f:
            conn.executescript(f.read())
        print(" Table created (if not exists)")

def add_record(name, email, phone):
    with connect_db() as conn:
        conn.execute("INSERT INTO records (name, email, phone) VALUES (?, ?, ?)",
                     (name, email, phone))
        conn.commit()
        print(" Record added successfully!")

def view_records():
    with connect_db() as conn:
        cursor = conn.execute("SELECT * FROM records")
        for row in cursor.fetchall():
            print(row)

def update_record(record_id, name, email, phone):
    with connect_db() as conn:
        conn.execute("UPDATE records SET name=?, email=?, phone=? WHERE id=?",
                     (name, email, phone, record_id))
        conn.commit()
        print("Record updated successfully!")

def delete_record(record_id):
    with connect_db() as conn:
        conn.execute("DELETE FROM records WHERE id=?", (record_id,))
        conn.commit()
        print(" Record deleted successfully!")

