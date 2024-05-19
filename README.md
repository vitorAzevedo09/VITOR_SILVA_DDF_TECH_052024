# VITOR_SILVA_DDF_TECH_052024

## Online Retail II Dataset

### Dataset Overview

#### Source
The Online Retail II dataset is publicly available and can be obtained from the UCI Machine Learning Repository or other similar repositories.

#### Description
- **Period Covered:** December 1, 2009, to December 9, 2011
- **Company Type:** UK-based online retail specializing in unique gift-ware
- **Customer Base:** Includes both retail customers and wholesalers
- **Number of Records:** Approximately 500,000 transactions

#### Key Columns
- **InvoiceNo:** Unique identifier for each transaction
- **StockCode:** Unique product code
- **Description:** Product description
- **Quantity:** Number of items purchased
- **InvoiceDate:** Date of the transaction
- **UnitPrice:** Price per unit of the product
- **CustomerID:** Unique identifier for each customer
- **Country:** Country of the customer

## Integrating and Loading Data from AWS S3 to Dadosfera

To integrate and load the Online Retail II dataset from AWS S3 into Dadosfera, I followed these steps:

### Step 1: Prepare the Dataset

Converted the dataset from XLSX to CSV format using a script.

### Step 2: Upload the Dataset to AWS S3

1. **Logged In to AWS Management Console:** Accessed the AWS Management Console and logged in with my credentials.
2. **Created an S3 Bucket:** Created a new S3 bucket.
3. **Uploaded the CSV File:**
   - Selected the bucket where I wanted to upload the data.
   - Clicked "Upload" and selected `online_retail_II.csv` from my local storage.
   - Followed the prompts to upload the file to the S3 bucket.

### Step 3: Configure Dadosfera to Connect to AWS S3

1. **Logged In to Dadosfera:** Accessed my Dadosfera account and logged in.
2. **Navigated to Data Ingestion Module:** Found and opened the data ingestion module on the Dadosfera platform.
3. **Created a New Dataset Project:**
   - Went to the data ingestion section.
   - Clicked on "Create New Dataset" or a similar option to start a new data project.

### Step 4: Connect to AWS S3

1. **Add S3 Connection:**
   - In the new dataset project, selected the option to add a data source.
   - Chose AWS S3 as the data source.
2. **Configure S3 Connection Details:**
   - Entered the necessary connection details, including my AWS Access Key, Secret Key, and the S3 bucket name where the dataset is stored.
   - Specified the path to the CSV file (e.g., `online_retail_II.csv`).

### Step 5: Load the Data into Dadosfera

1. **Schema Definition:**
   - Defined the schema based on the dataset columns:
     - `InvoiceNo` (String)
     - `StockCode` (String)
     - `Description` (String)
     - `Quantity` (Integer)
     - `InvoiceDate` (Date)
     - `UnitPrice` (Float)
     - `CustomerID` (String)
     - `Country` (String)

2. **Data Validation:**
   - Validated the dataset to ensure there were no errors or missing values.
   - Utilized Dadosfera's tools to automatically validate data types and formats.

3. **Initiate Data Load:**
   - Once the schema was defined and the data was validated, proceeded to load the data from AWS S3 into Dadosfera.
   - Monitored the loading process to ensure all records were successfully ingested.

4. **Verify the Data Load:**
   - After the data load was complete, verified the number of records loaded into Dadosfera.
   - Ensured that the dataset contained at least 100,000 records.

## Data Loading and Cataloging

### Data Cataloging

I used a script called `to_catalog_dataset.py` to send the most relevant dataset information via the Dadosfera API. This script automates the data cataloging process following best practices for data dictionary management.

#### Structure of the Script `to_catalog_dataset.py`

1. **Importing Libraries:**
   - Imported the `requests` library to make HTTP requests.

2. **API Credentials Configuration:**
   - Set the API credentials (`api_key` and `db_id`), which are passed as command-line arguments.

3. **Defining Dataset Information:**
   - Contained all relevant information, including name, description, and tags.

4. **Function to Catalog the Dataset:**
   - Defined a function that sends a POST request to the Dadosfera API with the dataset information.

5. **Script Execution:**
   - Executed the function to catalog the dataset.

## Data Quality Report using Great Expectations

### Data Quality Check Script with Great Expectations and AWS S3 Integration

I developed a custom script called `to_check_data_quality` that directly connects to our AWS S3 bucket using Great Expectations. This script streamlines the process of validating our data quality against predefined expectations. Here's an overview of how it works:

#### 1. Establishing Connection with AWS S3 Bucket

The script initiates a connection with our AWS S3 bucket, allowing seamless access to the data stored within. This connection is essential for retrieving the data that we want to assess for quality.

#### 2. Configuring Great Expectations

Once connected to the S3 bucket, the script configures Great Expectations to define expectations and validate our data. We specify the expectations that our data must meet, such as checking for null values, data types, or value ranges.

#### 3. Running Data Quality Checks

The script executes data quality checks using Great Expectations directly on the data stored in the S3 bucket. It validates the data against the defined expectations to ensure its integrity and reliability.

#### 4. Generating Validation Reports

After running the data quality checks, the script generates comprehensive validation reports. These reports provide insights into any discrepancies or issues found during the validation process, enabling us to identify and address data quality concerns promptly.

### Addressing Missing Values

Given that there are approximately 2,928 unique descriptions in the transaction dataset, with a total of 4,681 distinct values observed across more than 500,000 instances, it is advisable to address any null values in a strategic manner. One effective practice involves leveraging grouped features and algorithms such as KDD to impute synthetic data for missing values. This approach allows for the generation of meaningful data points based on patterns observed within specific groups or clusters, thereby enhancing the completeness and integrity of the dataset.
