# transformers.py
# Converts cleaned data into JSON and CSV formats.

import json
import csv

def create_phone_json(records):
    output = []

    for r in records:
        entry = {
            "first_name": r["first_name"],
            "phone_numbers": r["phone"].split(",")
        }
        output.append(entry)

    with open("export/customer_phone.json", "w") as json_file:
        json.dump(output, json_file, indent=4)

def create_location_csv(records):
    with open("export/customer_location.csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["first_name", "last_name", "county", "state"])

        for r in records:
            writer.writerow([
                r["first_name"],
                r["last_name"],
                r["county"],
                r["state"]
            ])
