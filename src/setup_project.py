import great_expectations as gx

from config import (
    CONTEXT_ROOT_DIR,
    DATASOURCE_NAME,
    DATA_ASSET_NAME,
    SUITE_NAME,
)

context = gx.get_context(context_root_dir=CONTEXT_ROOT_DIR)

# Add datasource for CSV files
datasource = context.sources.add_or_update_pandas_filesystem(
    name=DATASOURCE_NAME,
    base_directory="data"
)

# Add CSV asset
datasource.add_csv_asset(
    name=DATA_ASSET_NAME,
    batching_regex="customer_data.csv"
)

# Create expectation suite
context.add_or_update_expectation_suite(
    expectation_suite_name=SUITE_NAME
)

print("Great Expectations Part 1 setup completed.")
print(f"Datasource: {DATASOURCE_NAME}")
print(f"Data asset: {DATA_ASSET_NAME}")
print(f"Expectation suite: {SUITE_NAME}")