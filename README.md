# VITOR_SILVA_DDF_TECH_052024

#  Online Retail II Dataset

## Dataset Overview

### Source
The Online Retail II dataset is publicly available and can be obtained from the UCI Machine Learning Repository or other similar repositories.

### Description
- **Period Covered:** December 1, 2009, to December 9, 2011
- **Company Type:** UK-based online retail specializing in unique gift-ware
- **Customer Base:** Includes both retail customers and wholesalers
- **Number of Records:** Approximately 500,000 transactions

### Key Columns
- **InvoiceNo:** Unique identifier for each transaction
- **StockCode:** Unique product code
- **Description:** Product description
- **Quantity:** Number of items purchased
- **InvoiceDate:** Date of the transaction
- **UnitPrice:** Price per unit of the product
- **CustomerID:** Unique identifier for each customer
- **Country:** Country of the customer


## Integrating and Loading Data from AWS S3 to Dadosfera

To integrate and load the Online Retail II dataset from AWS S3 into Dadosfera, i followed these steps:

### Step 1: Prepared the Dataset conveting from xlsx to csv using script.

### Step 2: Upload Your Dataset to AWS S3

1. **Logeed In to AWS Management Console:** Accessed the AWS Management Console and logged in with my credentials.
2. **Created an S3 Bucket:** Create a new S3 bucket.
3. **Uploaded the CSV File:**
   - Selected the bucket where i want to upload the data.
   - Click "Upload" and select `online_retail_II.csv` from my local storage.
   - Followed the prompts to upload the file to the S3 bucket.

### Step 3: Configure Dadosfera to Connect to AWS S3

1. **Logged In to Dadosfera:** Accessed my Dadosfera account and logged in.
2. **Navigate to Data Ingestion Module:** Find and open the data ingestion module on the Dadosfera platform.
3. **Create a New Dataset Project:**
   - Go to the data ingestion section.
   - Click on "Create New Dataset" or a similar option to start a new data project.

### Step 4: Connect to AWS S3

1. **Add S3 Connection:**
   - In the new dataset project, select the option to add a data source.
   - Choose AWS S3 as the data source.
2. **Configure S3 Connection Details:**
   - Enter the necessary connection details, including your AWS Access Key, Secret Key, and the S3 bucket name where your dataset is stored.
   - Specify the path to the CSV file (e.g., `online_retail_II.csv`).

### Step 5: Load the Data into Dadosfera

1. **Schema Definition:**
   - Define the schema based on the dataset columns:
     - `InvoiceNo` (String)
     - `StockCode` (String)
     - `Description` (String)
     - `Quantity` (Integer)
     - `InvoiceDate` (Date)
     - `UnitPrice` (Float)
     - `CustomerID` (String)
     - `Country` (String)

2. **Data Validation:**
   - Validate the dataset to ensure there are no errors or missing values.
   - Dadosfera might provide tools to automatically validate data types and formats.

3. **Initiate Data Load:**
   - Once the schema is defined and the data is validated, proceed to load the data from AWS S3 into Dadosfera.
   - Monitor the loading process to ensure all records are successfully ingested.

4. **Verify the Data Load:**
   - After the data load is complete, verify the number of records loaded into Dadosfera.
   - Ensure that the dataset contains at least 100,000 records.

## Data Loading and Cataloging

### Data Cataloging

We use a script called `to_catalog_dataset.py` to send the most relevant dataset information via the Dadosfera API. This script automates the data cataloging process following best practices for data dictionary management.

#### Structure of the Script `to_catalog_dataset.py`

1. **Importing Libraries:**
   - Imports the `requests` library to make HTTP requests.

2. **API Credentials Configuration:**
   - Sets the API credentials (`api_key` and `db_id`), which are passed as command-line arguments.

3. **Defining Dataset Information:**
   - Contains all relevant information, including name, description, and tags.

4. **Function to Catalog the Dataset:**
   - Defines a function that sends a POST request to the Dadosfera API with the dataset information.

5. **Script Execution:**
   - Executes the function to catalog the dataset.

## Data Quality Report using Great Expectations

### Data Quality Check Script with Great Expectations and AWS S3 Integration

We've developed a custom script called `to_check_data_quality` that directly connects to our AWS S3 bucket using Great Expectations. This script streamlines the process of validating our data quality against predefined expectations. Here's an overview of how it works:

#### 1. Establishing Connection with AWS S3 Bucket

The script initiates a connection with our AWS S3 bucket, allowing seamless access to the data stored within. This connection is essential for retrieving the data that we want to assess for quality.

#### 2. Configuring Great Expectations

Once connected to the S3 bucket, the script configures Great Expectations to define expectations and validate our data. We specify the expectations that our data must meet, such as checking for null values, data types, or value ranges.

#### 3. Running Data Quality Checks

The script executes data quality checks using Great Expectations directly on the data stored in the S3 bucket. It validates the data against the defined expectations to ensure its integrity and reliability.

#### 4. Generating Validation Reports

After running the data quality checks, the script generates comprehensive validation reports. These reports provide insights into any discrepancies or issues found during the validation process, enabling us to identify and address data quality concerns promptly.



