# validation.py
# Simple validation functions for names, addresses, phones, etc.
# Nothing fancy, just clean checks.

import re

def validate_name(name):
    return bool(re.match(r"^[A-Za-z' -]+$", name))

def validate_company(company):
    # Company can't have weird symbols
    return not bool(re.search(r"[~`^{}|<>]", company))

def validate_address(address):
    return bool(re.match(r"^[A-Za-z0-9# ,.\-&()\\]+$", address))

def validate_city(city):
    return bool(re.match(r"^[A-Za-z ]+$", city))

def validate_state(state):
    valid_states = [
        "AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN",
        "MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA",
        "WA","WV","WI","WY"
    ]
    return state in valid_states

def validate_zip(zip_code):
    return bool(re.match(r"^\d{4,5}$", zip_code))

def validate_phone(phone):
    # Either 10 digits or 12 chars with dashes/periods
    return bool(re.match(r"^(\d{10}|[\d.-]{12})$", phone))

def validate_email(email):
    return bool(re.match(r"^[A-Za-z0-9._@+-]+$", email))
