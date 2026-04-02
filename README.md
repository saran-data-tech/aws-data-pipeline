# AWS Serverless Data Pipeline 

## What I Built
A serverless ETL data pipeline using AWS S3 and Lambda.
Raw data is automatically processed and analyzed without any servers.

## Architecture

data.csv → S3 Input Bucket → Lambda 1 → filtered_data.csv → Lambda 2 → final_report.csv


## AWS Services Used
- **S3** - Store raw and processed data
- **Lambda** - Run Python code serverlessly
- **IAM** - Manage permissions securely
- **S3 Trigger** - Auto trigger pipeline on file upload

## How It Works
1. Upload data.csv to S3 input bucket
2. Lambda 1 triggers automatically
3. Filters Chennai people only
4. Lambda 2 analyzes filtered data
5. Generates final report with average age

## What I Learned
- Serverless architecture
- ETL pipeline design
- AWS IAM permissions
- Chained Lambda functions
- Cloud data processing

## Data Cleaning (Python)
Cleaned raw data using Pandas library.

### Techniques used:
- Removed missing values
- Filled empty numbers with average
- Removed duplicate rows
- Fixed inconsistent text
- Reset index
