import pytest
import pandas as pd
from data_utils import load_csv, clean_phone, validate_email


def test_load_csv_success(tmp_path):
    file = tmp_path / "sample.csv"
    file.write_text("name,age\nAli,25\nSara,30")
    df = load_csv(file)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2


def test_load_csv_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_csv("missing_file.csv")


def test_load_csv_empty_file(tmp_path):
    file = tmp_path / "empty.csv"
    file.write_text("")
    with pytest.raises(Exception):
        load_csv(file)


def test_clean_phone_standard_formats():
    assert clean_phone("1234567890") == "123-456-7890"
    assert clean_phone("(123) 456-7890") == "123-456-7890"
    assert clean_phone("123-456-7890") == "123-456-7890"
    assert clean_phone("+1 123 456 7890") == "123-456-7890"


def test_clean_phone_invalid_inputs():
    assert clean_phone("12345") is None
    assert clean_phone("abc") is None
    assert clean_phone(None) is None


def test_validate_email_valid():
    assert validate_email("test@example.com") is True
    assert validate_email("student.name@seneca.ca") is True


def test_validate_email_invalid():
    assert validate_email("testexample.com") is False
    assert validate_email("test@") is False
    assert validate_email("@example.com") is False
    assert validate_email(None) is False