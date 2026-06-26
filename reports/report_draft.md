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

### Screenshot: Great Expectations Validation Results

![Great Expectations Validation Results](screenshots\gx_validation_results.png)

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

![Pytest Results](screenshots\pytest_results.png)

---

## 5. Reflection

The data quality issue that would most impact ML model performance is likely the salary-related problem. Salary is an important numerical feature that may strongly influence customer segmentation, prediction, or decision-making models. If salary values are missing, negative, or stored inconsistently as strings with dollar signs, the model may learn incorrect patterns or produce biased results.

Invalid email and phone formats are also important from a data operations perspective, but they may not directly affect model performance unless these fields are used as features. In contrast, salary and age are more likely to be used as predictive inputs, so errors in these columns can have a stronger impact on training quality and model reliability.

---

## 6. Conclusion

This assignment demonstrated how data validation can be integrated into an MLOps workflow. Great Expectations was used to define and run validation rules, while pytest was used to test reusable data utility functions. The project also includes automated report generation to make the validation process more reproducible and easier to maintain.
