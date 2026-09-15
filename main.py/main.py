# main.py
# Final project menu system

from book_functions import *
from database import Database
from data_import import load_raw_file
from transformers import create_phone_json, create_location_csv

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
            file_path = input("Enter file path: ")
            records = load_raw_file(file_path)

            if records:
                db.clear_table("customer_info")
                db.clear_table("customer_location")

                for r in records:
                    db.insert_record("customer_info", [
                        r["first_name"], r["last_name"], r["company"],
                        r["address"], r["city"], r["state"], r["zip_code"],
                        r["phone"], r["email"]
                    ])

                    db.insert_record("customer_location", [
                        r["first_name"], r["last_name"], r["county"], r["state"]
                    ])

                create_phone_json(records)
                create_location_csv(records)

                print("Import complete.")

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
