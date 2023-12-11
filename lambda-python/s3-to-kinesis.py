import boto3
import base64


# Define the AWS S3 bucket and object name
bucket_name = "my-bucket"
object_name = "my-object.txt"


def lambda_handler(event, context):

    # Create an empty list to store event data
    event_list = []

    # Iterate through each record in the event
    for record in event['Records']:

        # Decode the base64 encoded Kinesis data
        payload = base64.b64decode(record["kinesis"]["data"])

        # Append the decoded data to the event list
        event_list.append(payload)

    # Create an S3 client object
    s3_client = boto3.client('s3')

    # Upload the event data to the S3 bucket
    s3_client.put_object(Body=str(event_list), Bucket=bucket_name, Key=object_name)

    return "Successfully uploaded data to S3 bucket."
