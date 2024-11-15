import boto3
import json

# Initialize S3 client
s3 = boto3.client('s3')

# S3 bucket and file details
bucket_name = 'akyl-dev-employees'
file_key = 'employees.json'

try:
    # Fetch file from S3
    response = s3.get_object(Bucket=bucket_name, Key=file_key)
    data = response['Body'].read().decode('utf-8')
    
    # Load and print JSON data
    employees = json.loads(data)["employees"]
    print("Employee Data retrieved from S3:", employees)
except Exception as e:
    print("Error fetching data from S3:", e)
