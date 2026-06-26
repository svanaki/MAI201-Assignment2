import re
from pathlib import Path

import pandas as pd


def load_csv(filepath):
    path = Path(filepath)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {filepath}")

    df = pd.read_csv(path)

    if df.empty:
        raise ValueError("CSV file is empty.")

    return df


def clean_phone(phone):
    if pd.isna(phone):
        return None

    digits = re.sub(r"\D", "", str(phone))

    if len(digits) == 10:
        return f"{digits[:3]}-{digits[3:6]}-{digits[6:]}"
    if len(digits) == 11 and digits.startswith("1"):
        return f"{digits[1:4]}-{digits[4:7]}-{digits[7:]}"

    return None


def validate_email(email):
    if pd.isna(email):
        return False

    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return bool(re.match(pattern, str(email)))