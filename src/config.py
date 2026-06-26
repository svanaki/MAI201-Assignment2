from pathlib import Path

CONTEXT_ROOT_DIR = "gx"

DATASOURCE_NAME = "customer_data_source"
DATA_ASSET_NAME = "customer_data"
SUITE_NAME = "customer_data_expectations"

DATA_PATH = Path("data/customer_data.csv")

REPORTS_DIR = Path("reports")
VALIDATION_JSON_PATH = REPORTS_DIR / "validation_result.json"
QUALITY_SUMMARY_CSV_PATH = REPORTS_DIR / "data_quality_summary.csv"
REPORT_DRAFT_PATH = REPORTS_DIR / "report_draft.md"

FINAL_REPORT_PATH = Path("assignment2_report.md")

DATA_DOCS_PATH = Path("gx/uncommitted/data_docs/local_site/index.html")
GX_SCREENSHOT_PATH = Path("screenshots/gx_validation_results.png")
PYTEST_SCREENSHOT_PATH = Path("screenshots/pytest_results.png")

COURSE = "MAI201 MLOps"
ASSIGNMENT = "Assignment 2: Data Validation & Testing"
STUDENT_NAME = "Soodeh Vanaki"