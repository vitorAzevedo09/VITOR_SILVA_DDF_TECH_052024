import great_expectations as gx

context = gx.DataContext().create()

context.build_data_docs()


datasource = context.sources.add_or_update_pandas_s3(
    name="s3_datasource", bucket="ddftech052024"
)

asset = datasource.add_csv_asset(
    name="csv_retail_s3_asset",
    batching_regex=r"(.*\.csv)",
    s3_prefix="raw",
    s3_recursive_file_discovery=True
)

request = asset.build_batch_request()

context.add_or_update_expectation_suite(expectation_suite_name="online_retail_ii_suite")

validator = context.get_validator(
    batch_request=request, expectation_suite_name="online_retail_ii_suite"
)


# Define expectations
validator.expect_column_values_to_not_be_null(column="Country")
validator.expect_column_values_to_not_be_null(column="Invoice")
validator.expect_column_values_to_not_be_null(column="StockCode")
validator.expect_column_values_to_not_be_null(column="Quantity")
validator.expect_column_values_to_not_be_null(column="InvoiceDate")
validator.expect_column_values_to_not_be_null(column="Customer ID")

# Save the expectation suite
validator.save_expectation_suite(discard_failed_expectations=False)

# Run the checkpoint and generate a validation report
checkpoint_config = {
    "name": "online_retail_ii_suite_checkpoint",
    "config_version": 1.0,
    "class_name": "Checkpoint",
    "validations": [
        {
            "batch_request": request,
            "expectation_suite_name": "online_retail_ii_suite",
        }
    ],
}

context.add_or_update_checkpoint(**checkpoint_config)

# Execute the checkpoint
results = context.run_checkpoint(checkpoint_name="online_retail_ii_suite_checkpoint")

# Print a preview of the data
print(validator.head())

# Open the generated Data Docs (report) in your browser
context.open_data_docs()
