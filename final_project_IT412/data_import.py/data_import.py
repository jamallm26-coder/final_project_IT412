# data_import.py
# Handles reading the raw customer_export.txt file and cleaning the data.

import os
import shutil

def load_raw_file(file_path):
    if not os.path.exists(file_path):
        print("File not found.")
        return None

    # Backup before overwriting anything
    backup_path = "export/customer_export_backup.txt"
    shutil.copy(file_path, backup_path)

    cleaned_records = []

    with open(file_path, "r") as file:
        for line in file:
            parts = line.strip().split("|")

            # Expecting at least 10 fields, skip bad lines
            if len(parts) < 10:
                continue

            record = {
                "first_name": parts[0].strip(),
                "last_name": parts[1].strip(),
                "company": parts[2].strip(),
                "address": parts[3].strip(),
                "city": parts[4].strip(),
                "state": parts[5].strip(),
                "zip_code": parts[6].strip(),
                "county": parts[7].strip(),
                "phone": parts[8].strip(),
                "email": parts[9].strip()
            }

            cleaned_records.append(record)

    return cleaned_records
