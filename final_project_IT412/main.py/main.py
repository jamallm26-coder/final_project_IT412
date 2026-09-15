# main.py
# Basic menu system for interacting with the database.
# This will get expanded for the final project, but this is the starter version.

from book_functions import *
from database import Database

def menu():
    db = Database()

    while True:
        print("\n--- MAIN MENU ---")
        print("1. Import new data file")
        print("2. Show table data")
        print("3. Add a record")
        print("4. Edit a record")
        print("5. Delete a record")
        print("6. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            print("Import feature will be added in final project.")
        elif choice == "2":
            table = input("Which table? (customer_info / customer_location): ")
            show_table_data(table)
        elif choice == "3":
            table = input("Table name: ")
            fields = input("Enter fields separated by commas: ").split(",")
            add_record(table, fields)
        elif choice == "4":
            table = input("Table name: ")
            record_id = int(input("Record ID: "))
            field = input("Field to change: ")
            new_value = input("New value: ")
            edit_record(table, record_id, field, new_value)
        elif choice == "5":
            table = input("Table name: ")
            record_id = int(input("Record ID: "))
            delete_record(table, record_id)
        elif choice == "6":
            print("Goodbye.")
            db.close()
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    menu()
