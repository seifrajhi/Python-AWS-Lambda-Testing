import pytest
import boto3
from main import lambda_handler

def test_lambda_handler(s3_mock, aws_credentials):
    # Event and Context are not used in this example
    event = {}
    context = {}

    # Invoke the Lambda function
    response = lambda_handler(event, context)

    # Check if the S3 object was created successfully
    assert response["statusCode"] == 200

    # Check if the object exists in S3
    objects = s3_mock.list_objects(Bucket='your-s3-bucket')
    assert objects["Contents"][0]["Key"] == "example.txt"
