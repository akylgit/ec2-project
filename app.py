from flask import Flask, jsonify
from flask_cors import CORS
import boto3
import json

app = Flask(__name__)
CORS(app)

@app.route('/employees', methods=['GET'])
def get_employees():
    s3 = boto3.client('s3')
    bucket_name = 'your-bucket-name'
    file_key = 'employees.json'
    try:
        response = s3.get_object(Bucket=bucket_name, Key=file_key)
        data = response['Body'].read().decode('utf-8')
        employees = json.loads(data)
        return jsonify(employees)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
