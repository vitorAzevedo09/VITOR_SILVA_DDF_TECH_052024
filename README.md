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
