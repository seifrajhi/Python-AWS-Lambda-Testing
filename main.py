import boto3

def lambda_handler(event, context):
    # Sample Lambda function that manipulates data and uploads to S3
    data_to_upload = "Hello, Moto!"

    # AWS S3 Configuration
    s3_bucket = "your-s3-bucket"
    s3_key = "example.txt"

    # Upload to S3
    s3 = boto3.client("s3")
    s3.put_object(Body=data_to_upload, Bucket=s3_bucket, Key=s3_key)

    return {"statusCode": 200, "body": "Data uploaded to S3 successfully."}
