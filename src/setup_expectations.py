import great_expectations as gx

context = gx.get_context(context_root_dir="gx")

datasource_name = "customer_data_source"
data_asset_name = "customer_data"
suite_name = "customer_data_expectations"

# Add datasource for CSV files
datasource = context.sources.add_pandas_filesystem(
    name=datasource_name,
    base_directory="data"
)

# Add CSV asset
datasource.add_csv_asset(
    name=data_asset_name,
    batching_regex="customer_data.csv"
)

# Create expectation suite
context.add_or_update_expectation_suite(
    expectation_suite_name=suite_name
)

print("Great Expectations Part 1 setup completed.")
print(f"Datasource: {datasource_name}")
print(f"Data asset: {data_asset_name}")
print(f"Expectation suite: {suite_name}")