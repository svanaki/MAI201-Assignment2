# Assignment 2: Data Validation & Testing

**Course:** MAI201 MLOps  
**Student:** Soodeh Vanaki  
**Date:** June 26, 2026

---

## 1. Overview

This report summarizes the data validation and testing work completed for Assignment 2. The dataset was validated using Great Expectations, and additional data quality issue counts were generated using a Python validation pipeline.

The validation failed because the messy customer dataset contains multiple data quality issues, including missing values, duplicate customer records, invalid email formats, invalid country values, out-of-range ages, negative salary values, and invalid signup dates.

The project was developed using a Git feature-branch workflow, with each assignment part implemented and merged through separate pull requests.

---

## 2. Great Expectations Validation Results

The Great Expectations expectation suite was created using the suite name:

`customer_data_expectations`

The validation results were saved as:

`reports/validation_result.json`

The generated HTML Data Docs are available locally at:

`gx\uncommitted\data_docs\local_site\index.html`

### Screenshot: Command-Line Validation Summary

![Command-Line Validation Summary](screenshots\gx_validation_results.png)

### Screenshot: Great Expectations HTML Data Docs Overview

![Great Expectations HTML Overview](screenshots\gx_html_overview.png)

### Screenshot: Great Expectations Row Count Expectation Results

![Great Expectations Row Count Expectation Results](screenshots\gx_html_row_count.png)

### Screenshot: Great Expectations Age Expectation Results

![Great Expectations Age Expectation Results](screenshots\gx_html_age.png)

### Screenshot: Great Expectations Country Expectation Results

![Great Expectations Country Expectation Results](screenshots\gx_html_country.png)

### Screenshot: Great Expectations Customer ID Expectation Results

![Great Expectations Customer ID Expectation Results](screenshots\gx_html_customer_id.png)

### Screenshot: Great Expectations Email Expectation Results

![Great Expectations Email Expectation Results](screenshots\gx_html_email.png)

### Screenshot: Great Expectations Salary Expectation Results

![Great Expectations Salary Expectation Results](screenshots\gx_html_salary.png)

### Screenshot: Great Expectations Signup Date Expectation Results

![Great Expectations Signup Date Expectation Results](screenshots\gx_html_signup_date.png)

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

Among all the detected data quality issues, the **salary-related problems** would have the greatest impact on machine learning model performance. Salary is an important numerical feature that is commonly used in predictive models, customer segmentation, and business analytics. Missing values, negative salaries, and inconsistent formatting (such as values stored with dollar signs) can distort the underlying data distribution and lead to inaccurate model training.

Although duplicate customer IDs and invalid email formats also reduce data quality, they primarily affect data integrity and operational processes. In contrast, poor-quality salary data directly influences feature values that many machine learning algorithms rely on, making it the most significant issue for model accuracy and generalization.

This assignment highlights the importance of validating data before it enters a machine learning pipeline. Detecting and correcting data quality issues early helps improve model reliability, reduces bias, and prevents errors from propagating into downstream analytics and decision-making systems.


---

## 6. Conclusion

This assignment successfully implemented a complete data validation workflow using Great Expectations and pytest. A Great Expectations project was configured, an expectation suite containing eight validation rules was created, and the dataset was validated against those rules. Automated reports were generated, including JSON results, HTML Data Docs, and a Markdown report summarizing the detected data quality issues.

In addition, pytest was used to verify the correctness of the supporting data utility functions. Together, these components demonstrate how automated validation and testing can improve data quality and reliability within an MLOps pipeline before machine learning models are trained.
