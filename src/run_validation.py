import json
from pathlib import Path

import pandas as pd
import great_expectations as gx


CONTEXT_ROOT_DIR = "gx"
DATASOURCE_NAME = "customer_data_source"
DATA_ASSET_NAME = "customer_data"
SUITE_NAME = "customer_data_expectations"

DATA_PATH = Path("data/customer_data.csv")
REPORTS_DIR = Path("reports")
VALIDATION_RESULT_PATH = REPORTS_DIR / "validation_result.json"
QUALITY_SUMMARY_PATH = REPORTS_DIR / "data_quality_summary.csv"


def clean_salary(value):
    if pd.isna(value):
        return None
    value = str(value).replace("$", "").replace(",", "").strip()
    try:
        return float(value)
    except ValueError:
        return None


def load_dataset(path):
    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")
    return pd.read_csv(path)


def count_quality_issues(df):
    email_pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    age_numeric = pd.to_numeric(df["age"], errors="coerce")
    salary_numeric = df["salary"].apply(clean_salary)
    signup_dates = pd.to_datetime(df["signup_date"], errors="coerce")

    return {
        "Missing age": int(df["age"].isna().sum()),
        "Missing email": int(df["email"].isna().sum()),
        "Missing salary": int(df["salary"].isna().sum()),
        "Duplicate customer_id": int(df["customer_id"].duplicated().sum()),
        "Age outside 0-120": int(((age_numeric < 0) | (age_numeric > 120)).sum()),
        "Negative salary": int((salary_numeric < 0).sum()),
        "Invalid email format": int(
            (~df["email"].fillna("").astype(str).str.match(email_pattern)).sum()
        ),
        "Invalid country": int(
            (~df["country"].isin(["USA", "Canada", "UK", "Australia"])).sum()
        ),
        "Invalid signup_date": int(signup_dates.isna().sum()),
    }


def run_great_expectations():
    context = gx.get_context(context_root_dir=CONTEXT_ROOT_DIR)

    validator = context.get_validator(
        datasource_name=DATASOURCE_NAME,
        data_asset_name=DATA_ASSET_NAME,
        expectation_suite_name=SUITE_NAME,
    )

    checkpoint = context.add_or_update_checkpoint(
        name="customer_data_checkpoint",
        validator=validator,
    )

    validation_result = checkpoint.run()
    context.build_data_docs()

    return validation_result


def save_json_report(validation_result):
    REPORTS_DIR.mkdir(exist_ok=True)

    with open(VALIDATION_RESULT_PATH, "w", encoding="utf-8") as file:
        json.dump(validation_result.to_json_dict(), file, indent=4)


def save_quality_summary_csv(issues):
    REPORTS_DIR.mkdir(exist_ok=True)

    summary_df = pd.DataFrame(
        [{"Issue": issue, "Count": count} for issue, count in issues.items()]
    )

    summary_df.to_csv(QUALITY_SUMMARY_PATH, index=False)


def print_summary(df, issues, validation_result):
    print("=" * 60)
    print("DATA QUALITY VALIDATION SUMMARY")
    print("=" * 60)

    print(f"Rows                  : {len(df)}")
    print(f"Overall Status        : {'PASSED' if validation_result.success else 'FAILED'}")

    print("\nIssue Summary")
    print("-" * 60)
    for issue, count in issues.items():
        print(f"{issue:<25}: {count}")

    print("\nGenerated Reports")
    print("-" * 60)
    print(f"JSON report           : {VALIDATION_RESULT_PATH}")
    print(f"CSV summary           : {QUALITY_SUMMARY_PATH}")
    print("HTML Data Docs        : gx/uncommitted/data_docs/local_site/index.html")
    print("=" * 60)


def main():
    df = load_dataset(DATA_PATH)
    issues = count_quality_issues(df)

    validation_result = run_great_expectations()

    save_json_report(validation_result)
    save_quality_summary_csv(issues)
    print_summary(df, issues, validation_result)


if __name__ == "__main__":
    main()