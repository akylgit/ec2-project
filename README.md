README.md
This file provides an overview and setup instructions for the project.

# Employee Directory App with AWS EC2 and S3 Integration

This project is a simple employee directory web application that retrieves and displays employee data stored in an AWS S3 bucket. The project is built using a Flask backend to fetch data from S3, and a JavaScript-based frontend to display employee information.

## Project Structure

. ├── app.py # Flask backend server file ├── frontend # Folder for frontend files │ ├── index.html │ ├── style.css │ └── script.js ├── requirements.txt # Dependencies (Flask, boto3, etc.) └── README.md # Project documentation



## Prerequisites

- AWS CLI configured with necessary permissions to access S3 and EC2.
- An S3 bucket containing `employees.json` with sample employee data.
- Python 3 and `pip` installed on your EC2 instance or local environment.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/aidiko20/ec2-s3-app.git
cd ec2-s3-app

2. Install Dependencies
Navigate to the project root directory and install the required Python packages:
pip install -r requirements.txt

3. Configure AWS S3 Bucket and IAM Role
Ensure your AWS IAM role has AmazonS3ReadOnlyAccess permissions.

Upload employees.json to your S3 bucket in the following format:


{
  "employees": [
    {"id": 1, "name": "Alice Johnson", "position": "Software Engineer", "department": "Engineering"},
    {"id": 2, "name": "Bob Smith", "position": "DevOps Engineer", "department": "Operations"},
    {"id": 3, "name": "Carol White", "position": "Product Manager", "department": "Product"},
    {"id": 4, "name": "David Brown", "position": "Data Scientist", "department": "Data"},
    {"id": 5, "name": "Emma Davis", "position": "UX Designer", "department": "Design"}
  ]
}
4. Set Up and Run the Flask Server
Update app.py with your S3 bucket name, then start the Flask server:


python app.py
This will start the server on http://0.0.0.0:5000, making it accessible on your EC2 instance.

5. Access the Frontend
Open frontend/index.html in a browser or set up a web server to serve the file, and replace apiUrl in script.js with your EC2’s public IP and port 5000.

Usage
Show One Employee: Click on "Show Employee" to display a random employee.
Show All Employees: Click on "Show All Employees" to list all employees.
License
This project is open source and available under the MIT License.






