import pytest
import pandas as pd

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from data_utils import load_csv, clean_phone, validate_email


def test_load_csv_success(tmp_path):
    file_path = tmp_path / "sample.csv"
    file_path.write_text("name,age\nAlice,25\nBob,30")

    df = load_csv(file_path)

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2
    assert list(df.columns) == ["name", "age"]


def test_load_csv_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_csv("missing_file.csv")


def test_load_csv_empty_file(tmp_path):
    file_path = tmp_path / "empty.csv"
    file_path.write_text("")

    with pytest.raises(Exception):
        load_csv(file_path)


def test_clean_phone_standard_formats():
    assert clean_phone("1234567890") == "123-456-7890"
    assert clean_phone("(123) 456-7890") == "123-456-7890"
    assert clean_phone("123-456-7890") == "123-456-7890"
    assert clean_phone("+1 123 456 7890") == "123-456-7890"


def test_clean_phone_invalid_inputs():
    assert clean_phone("12345") is None
    assert clean_phone("abc") is None
    assert clean_phone(None) is None
    
    
def test_clean_phone_with_spaces():
    assert clean_phone("123 456 7890") == "123-456-7890"


def test_validate_email_valid():
    assert validate_email("test@example.com") is True
    assert validate_email("student.name@seneca.ca") is True


def test_validate_email_invalid():
    assert validate_email("testexample.com") is False
    assert validate_email("test@") is False
    assert validate_email("@example.com") is False
    assert validate_email(None) is False
    
    
def test_validate_email_uppercase():
    assert validate_email("JOHN@EXAMPLE.COM") is True