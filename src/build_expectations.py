import great_expectations as gx

from config import (
    CONTEXT_ROOT_DIR,
    DATASOURCE_NAME,
    DATA_ASSET_NAME,
    SUITE_NAME,
)


def main():
    context = gx.get_context(context_root_dir=CONTEXT_ROOT_DIR)

    validator = context.get_validator(
        datasource_name=DATASOURCE_NAME,
        data_asset_name=DATA_ASSET_NAME,
        expectation_suite_name=SUITE_NAME,
    )

    validator.expect_column_values_to_not_be_null("customer_id")
    validator.expect_column_values_to_be_unique("customer_id")

    validator.expect_column_values_to_be_between(
        column="age",
        min_value=0,
        max_value=120,
    )

    validator.expect_column_values_to_match_regex(
        column="email",
        regex=r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$",
    )

    validator.expect_column_values_to_not_be_null(
        column="salary",
        mostly=0.95,
    )

    validator.expect_column_values_to_be_in_set(
        column="country",
        value_set=["USA", "Canada", "UK", "Australia"],
    )

    validator.expect_column_values_to_be_dateutil_parseable(
        column="signup_date",
    )

    validator.expect_table_row_count_to_be_between(
        min_value=500,
        max_value=1000,
    )

    validator.save_expectation_suite(discard_failed_expectations=False)

    print("Expectation suite built successfully.")
    print(f"Suite name: {SUITE_NAME}")


if __name__ == "__main__":
    main()