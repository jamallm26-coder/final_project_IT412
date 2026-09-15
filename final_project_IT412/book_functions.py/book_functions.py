# book_functions.py
# Helper functions for showing, adding, editing, and deleting records.
# Using the database class and keeping everything simple.

from database import Database
from validation import *

db = Database()

def show_table_data(table):
    records = db.fetch_all(table)
    for row in records:
        print(row)

def add_record(table, data):
    db.insert_record(table, data)
    print("Record added.")

def edit_record(table, record_id, field, new_value):
    db.update_record(table, record_id, field, new_value)
    print("Record updated.")

def delete_record(table, record_id):
    confirm = input("Delete this record? (Y/N): ")
    if confirm.lower() == "y":
        db.delete_record(table, record_id)
        print("Record deleted.")
    else:
        print("Cancelled.")
