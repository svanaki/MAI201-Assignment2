import re
import pandas as pd


def load_csv(filepath):
    try:
        df = pd.read_csv(filepath)
    except FileNotFoundError:
        raise FileNotFoundError("File not found.")

    if df.empty:
        raise ValueError("CSV file is empty.")

    return df


def clean_phone(phone):
    if pd.isna(phone):
        return None

    digits = re.sub(r"\D", "", str(phone))

    if len(digits) == 10:
        return f"{digits[:3]}-{digits[3:6]}-{digits[6:]}"
    elif len(digits) == 11 and digits.startswith("1"):
        return f"{digits[1:4]}-{digits[4:7]}-{digits[7:]}"
    else:
        return None


def validate_email(email):
    if pd.isna(email):
        return False

    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return bool(re.match(pattern, str(email)))