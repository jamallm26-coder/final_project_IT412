# database.py
# Basic database setup for storing customer info and location data.
# Keeping this simple and readable.

import sqlite3

class Database:
    def __init__(self, db_name="customer_data.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self):
        # First table: full customer info
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS customer_info (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            company TEXT,
            address TEXT,
            city TEXT,
            state TEXT,
            zip_code TEXT,
            phone TEXT,
            email TEXT
        )
        """)

        # Second table: location‑only data
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS customer_location (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            county TEXT,
            state TEXT
        )
        """)

        self.conn.commit()

    def insert_record(self, table, data):
        # Insert a new record into whichever table we choose
        placeholders = ", ".join(["?"] * len(data))
        query = f"INSERT INTO {table} VALUES (NULL, {placeholders})"
        self.cursor.execute(query, data)
        self.conn.commit()

    def fetch_all(self, table):
        # Grab everything from a table
        self.cursor.execute(f"SELECT * FROM {table}")
        return self.cursor.fetchall()

    def update_record(self, table, record_id, field, new_value):
        # Update one field on one record
        query = f"UPDATE {table} SET {field} = ? WHERE id = ?"
        self.cursor.execute(query, (new_value, record_id))
        self.conn.commit()

    def delete_record(self, table, record_id):
        # Delete a record by ID
        query = f"DELETE FROM {table} WHERE id = ?"
        self.cursor.execute(query, (record_id,))
        self.conn.commit()

    def clear_table(self, table):
        # Wipe a table clean before importing new data
        self.cursor.execute(f"DELETE FROM {table}")
        self.conn.commit()

    def close(self):
        self.conn.close()
