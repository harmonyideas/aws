import boto3
import json

s3 = boto3.client('s3')
kinesis = boto3.client('kinesis')

def lambda_handler(event, context):

    if event:
        # Extract bucket name and filename from event record
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        filename = event['Records'][0]['s3']['object']['key']

        # Download file object from S3
        file_obj = s3.get_object(Bucket=bucket_name, Key=filename)

        # Read and decode file content
        file_content = file_obj['Body'].read().decode('utf-8')

        # Prepare Kinesis record
        data = bytes(file_content, 'utf-8')
        partition_key = 'my_partition_key'
        stream_name = 'my_stream_name'

        # Put record to Kinesis stream
        kinesis.put_record(Data=data, StreamName=stream_name, PartitionKey=partition_key)

        return "Successfully uploaded data to Kinesis stream."
    else:
        return "No event received."
