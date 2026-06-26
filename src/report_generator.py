from datetime import date

import pandas as pd

from config import (
    QUALITY_SUMMARY_CSV_PATH,
    DATA_DOCS_PATH,
    GX_SCREENSHOT_PATH,
    PYTEST_SCREENSHOT_PATH,
    REPORT_DRAFT_PATH,
    FINAL_REPORT_PATH,
    COURSE,
    ASSIGNMENT, 
    STUDENT_NAME,
)

def load_quality_summary():
    if not QUALITY_SUMMARY_CSV_PATH.exists():
        raise FileNotFoundError(
            f"Missing quality summary file: {QUALITY_SUMMARY_CSV_PATH}. "
            "Run src/run_validation.py first."
        )

    return pd.read_csv(QUALITY_SUMMARY_CSV_PATH)


def build_markdown_table(summary_df):
    return summary_df.to_markdown(index=False)


def get_total_issues(summary_df):
    return int(summary_df["Count"].sum())


def get_highest_issue(summary_df):
    highest = summary_df.sort_values("Count", ascending=False).iloc[0]
    return highest["Issue"], int(highest["Count"])


def build_report(summary_df):
    today = date.today().strftime("%B %d, %Y")
    total_issues = get_total_issues(summary_df)
    highest_issue, highest_count = get_highest_issue(summary_df)
    markdown_table = build_markdown_table(summary_df)

    return f"""# {ASSIGNMENT}

**Course:** {COURSE}  
**Student:** {STUDENT_NAME}  
**Date:** {today}

---

## 1. Overview

This report summarizes the data validation and testing work completed for Assignment 2. The dataset was validated using Great Expectations, and additional data quality issue counts were generated using a Python validation pipeline.

The validation failed because the messy customer dataset contains multiple data quality issues, including missing values, duplicate customer records, invalid email formats, invalid country values, out-of-range ages, negative salary values, and invalid signup dates.

---

## 2. Great Expectations Validation Results

The Great Expectations expectation suite was created using the suite name:

`customer_data_expectations`

The validation results were saved as:

`reports/validation_result.json`

The generated HTML Data Docs are available locally at:

`{DATA_DOCS_PATH}`

### Screenshot: Great Expectations Validation Results

![Great Expectations Validation Results]({GX_SCREENSHOT_PATH})

---

## 3. Data Quality Issues Found

The validation pipeline identified the following data quality issues:

{markdown_table}

**Total detected data quality issues:** {total_issues}

The most frequent issue was **{highest_issue}**, with **{highest_count}** affected rows.

---

## 4. Pytest Unit Test Results

Unit tests were written for the following utility functions:

- `load_csv(filepath)`
- `clean_phone(phone)`
- `validate_email(email)`

The pytest execution screenshot is included below.

### Screenshot: Pytest Results

![Pytest Results]({PYTEST_SCREENSHOT_PATH})

---

## 5. Reflection

The data quality issue that would most impact ML model performance is likely the salary-related problem. Salary is an important numerical feature that may strongly influence customer segmentation, prediction, or decision-making models. If salary values are missing, negative, or stored inconsistently as strings with dollar signs, the model may learn incorrect patterns or produce biased results.

Invalid email and phone formats are also important from a data operations perspective, but they may not directly affect model performance unless these fields are used as features. In contrast, salary and age are more likely to be used as predictive inputs, so errors in these columns can have a stronger impact on training quality and model reliability.

---

## 6. Conclusion

This assignment demonstrated how data validation can be integrated into an MLOps workflow. Great Expectations was used to define and run validation rules, while pytest was used to test reusable data utility functions. The project also includes automated report generation to make the validation process more reproducible and easier to maintain.
"""


def write_report(content, path):
    path.parent.mkdir(exist_ok=True) if path.parent != path else None

    with open(path, "w", encoding="utf-8") as file:
        file.write(content)


def generate_report():
    summary_df = load_quality_summary()
    report_content = build_report(summary_df)

    write_report(report_content, REPORT_DRAFT_PATH)
    write_report(report_content, FINAL_REPORT_PATH)

    print(f"Draft report generated: {REPORT_DRAFT_PATH}")
    print(f"Final report generated: {FINAL_REPORT_PATH}")


if __name__ == "__main__":
    generate_report()