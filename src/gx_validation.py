import great_expectations as gx


CONTEXT_ROOT_DIR = "gx"
DATASOURCE_NAME = "customer_data_source"
DATA_ASSET_NAME = "customer_data"
SUITE_NAME = "customer_data_expectations"


def main():
    context = gx.get_context(context_root_dir=CONTEXT_ROOT_DIR)

    validator = context.get_validator(
        datasource_name=DATASOURCE_NAME,
        data_asset_name=DATA_ASSET_NAME,
        expectation_suite_name=SUITE_NAME,
    )

    # 1. customer_id must not be null
    validator.expect_column_values_to_not_be_null("customer_id")

    # 2. customer_id must be unique
    validator.expect_column_values_to_be_unique("customer_id")

    # 3. age must be between 0 and 120
    validator.expect_column_values_to_be_between(
        column="age",
        min_value=0,
        max_value=120,
    )

    # 4. email must match a valid email format
    validator.expect_column_values_to_match_regex(
        column="email",
        regex=r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$",
    )

    # 5. salary must be present in at least 95% of rows
    validator.expect_column_values_to_not_be_null(
        column="salary",
        mostly=0.95,
    )

    # 6. country must be one of the allowed values
    validator.expect_column_values_to_be_in_set(
        column="country",
        value_set=["USA", "Canada", "UK", "Australia"],
    )

    # 7. signup_date must be datetime type
    validator.expect_column_values_to_be_dateutil_parseable(
        column="signup_date",
    )

    # 8. row count must be between 500 and 1000
    validator.expect_table_row_count_to_be_between(
        min_value=500,
        max_value=1000,
    )

    validator.save_expectation_suite(discard_failed_expectations=False)

    print("Part 2 completed: expectations were added successfully.")
    print(f"Expectation suite saved as: {SUITE_NAME}")


if __name__ == "__main__":
    main()