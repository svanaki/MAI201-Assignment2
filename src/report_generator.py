from datetime import date

import pandas as pd

from config import (
    QUALITY_SUMMARY_CSV_PATH,
    DATA_DOCS_PATH,
    GX_SCREENSHOT_PATH,
    PYTEST_SCREENSHOT_PATH,
    REPORT_DRAFT_PATH,
    COURSE,
    ASSIGNMENT,
    STUDENT_NAME,
    GX_HTML_OVERVIEW_SCREENSHOT_PATH,
    GX_HTML_AGE_SCREENSHOT_PATH,
    GX_HTML_COUNTRY_SCREENSHOT_PATH,
    GX_HTML_CUSTOMER_ID_SCREENSHOT_PATH,
    GX_HTML_EMAIL_SCREENSHOT_PATH,
    GX_HTML_SALARY_SCREENSHOT_PATH,
    GX_HTML_ROW_COUNT_SCREENSHOT_PATH,
    GX_HTML_SIGNUP_DATE_SCREENSHOT_PATH,
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

### Screenshot: Command-Line Validation Summary

![Command-Line Validation Summary]({GX_SCREENSHOT_PATH.as_posix()})

### Screenshot: Great Expectations HTML Data Docs Overview

![Great Expectations HTML Overview]({GX_HTML_OVERVIEW_SCREENSHOT_PATH.as_posix()})

### Screenshot: Great Expectations Age Expectation Results

![Great Expectations Age Expectation Results]({GX_HTML_AGE_SCREENSHOT_PATH.as_posix()})

### Screenshot: Great Expectations Country Expectation Results

![Great Expectations Country Expectation Results]({GX_HTML_COUNTRY_SCREENSHOT_PATH.as_posix()})

### Screenshot: Great Expectations Customer ID Expectation Results

![Great Expectations Customer ID Expectation Results]({GX_HTML_CUSTOMER_ID_SCREENSHOT_PATH.as_posix()})

### Screenshot: Great Expectations Email Expectation Results

![Great Expectations Email Expectation Results]({GX_HTML_EMAIL_SCREENSHOT_PATH.as_posix()})

### Screenshot: Great Expectations Salary Expectation Results

![Great Expectations Salary Expectation Results]({GX_HTML_SALARY_SCREENSHOT_PATH.as_posix()})

### Screenshot: Great Expectations Row Count Expectation Results

![Great Expectations Row Count Expectation Results]({GX_HTML_ROW_COUNT_SCREENSHOT_PATH.as_posix()})

### Screenshot: Great Expectations Signup Date Expectation Results

![Great Expectations Signup Date Expectation Results]({GX_HTML_SIGNUP_DATE_SCREENSHOT_PATH.as_posix()})

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

![Pytest Results]({PYTEST_SCREENSHOT_PATH.as_posix()})

---

## 5. Reflection

The data quality issue that would most impact ML model performance is likely the salary-related problem. Salary is an important numerical feature that may strongly influence customer segmentation, prediction, or decision-making models. If salary values are missing, negative, stored inconsistently as strings with dollar signs, or include unrealistic values, the model may learn incorrect patterns and produce unreliable predictions.

Duplicate customer records are also important because they can overrepresent some customers and bias model training. Invalid email formats and phone number inconsistencies are especially important for data operations and customer communication, although they may have less direct model impact unless those fields are used for feature engineering.

Overall, validation is important because poor-quality data can create misleading patterns before the model training stage begins.

---

## 6. Conclusion

This assignment demonstrated how data validation can be integrated into an MLOps workflow. Great Expectations was used to define and run validation rules, while pytest was used to test reusable data utility functions. The project also includes automated report generation to make the validation process more reproducible and easier to maintain.
"""


def write_report(content, path):
    path.parent.mkdir(exist_ok=True)

    with open(path, "w", encoding="utf-8") as file:
        file.write(content)


def generate_report():
    summary_df = load_quality_summary()
    report_content = build_report(summary_df)

    write_report(report_content, REPORT_DRAFT_PATH)

    print(f"Draft report generated: {REPORT_DRAFT_PATH}")
    print("Final report was not overwritten. Copy the draft content into assignment2_report.md when ready and modify as needed.")


if __name__ == "__main__":
    generate_report()