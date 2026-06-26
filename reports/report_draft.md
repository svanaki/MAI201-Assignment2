# Assignment 2: Data Validation & Testing

**Course:** MAI201 MLOps  
**Student:** Soodeh Vanaki  
**Date:** June 26, 2026

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

`gx\uncommitted\data_docs\local_site\index.html`

### Screenshot: Command-Line Validation Summary

![Command-Line Validation Summary](screenshots/gx_validation_results.png)

### Screenshot: Great Expectations HTML Data Docs Overview

![Great Expectations HTML Overview](screenshots/gx_html_overview.png)

### Screenshot: Great Expectations Age Expectation Results

![Great Expectations Age Expectation Results](screenshots/gx_html_age.png)

### Screenshot: Great Expectations Country Expectation Results

![Great Expectations Country Expectation Results](screenshots/gx_html_country.png)

### Screenshot: Great Expectations Customer ID Expectation Results

![Great Expectations Customer ID Expectation Results](screenshots/gx_html_customer_id.png)

### Screenshot: Great Expectations Email Expectation Results

![Great Expectations Email Expectation Results](screenshots/gx_html_email.png)

### Screenshot: Great Expectations Salary Expectation Results

![Great Expectations Salary Expectation Results](screenshots/gx_html_salary.png)

### Screenshot: Great Expectations Row Count Expectation Results

![Great Expectations Row Count Expectation Results](screenshots/gx_html_row_count.png)

### Screenshot: Great Expectations Signup Date Expectation Results

![Great Expectations Signup Date Expectation Results](screenshots/gx_html_signup_date.png)

---

## 3. Data Quality Issues Found

The validation pipeline identified the following data quality issues:

| Issue                 |   Count |
|:----------------------|--------:|
| Missing age           |     147 |
| Missing email         |     438 |
| Missing salary        |     425 |
| Duplicate customer_id |     452 |
| Age outside 0-120     |     384 |
| Negative salary       |     159 |
| Invalid email format  |     784 |
| Invalid country       |     342 |
| Invalid signup_date   |     256 |

**Total detected data quality issues:** 3387

The most frequent issue was **Invalid email format**, with **784** affected rows.

---

## 4. Pytest Unit Test Results

Unit tests were written for the following utility functions:

- `load_csv(filepath)`
- `clean_phone(phone)`
- `validate_email(email)`

The pytest execution screenshot is included below.

### Screenshot: Pytest Results

![Pytest Results](screenshots/pytest_results.png)

---

## 5. Reflection

The data quality issue that would most impact ML model performance is likely the salary-related problem. Salary is an important numerical feature that may strongly influence customer segmentation, prediction, or decision-making models. If salary values are missing, negative, stored inconsistently as strings with dollar signs, or include unrealistic values, the model may learn incorrect patterns and produce unreliable predictions.

Duplicate customer records are also important because they can overrepresent some customers and bias model training. Invalid email formats and phone number inconsistencies are especially important for data operations and customer communication, although they may have less direct model impact unless those fields are used for feature engineering.

Overall, validation is important because poor-quality data can create misleading patterns before the model training stage begins.

---

## 6. Conclusion

This assignment demonstrated how data validation can be integrated into an MLOps workflow. Great Expectations was used to define and run validation rules, while pytest was used to test reusable data utility functions. The project also includes automated report generation to make the validation process more reproducible and easier to maintain.
