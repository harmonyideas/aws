import base64
import csv
import io
import os

import boto3

# The region comes from AWS_REGION, which Lambda sets automatically.
# us-east-1 is only a fallback for running outside Lambda.
region = os.environ.get("AWS_REGION", "us-east-1")

# Accessing resources
s3 = boto3.resource('s3', region_name=region)
dynamodb = boto3.resource('dynamodb', region_name=region)
table = dynamodb.Table('my_table')


def lambda_handler(event, context):
    # Process every Kinesis record, not only the last one
    for record in event['Records']:
        # Decode Kinesis data
        payload = base64.b64decode(record['kinesis']['data']).decode('utf-8')

        # Parse the CSV payload. csv.reader handles \r\n line endings and a
        # missing trailing newline, so the last row is not dropped.
        reader = csv.reader(io.StringIO(payload))
        keys = next(reader, None)
        if not keys:
            continue

        with table.batch_writer() as batch:
            for values in reader:
                # Skip blank lines
                if not any(value.strip() for value in values):
                    continue

                item = {}
                for key, value in zip(keys, values):
                    # Omit empty values rather than writing a placeholder
                    if value == '':
                        continue
                    item[key] = int(value) if key == 'my_id' else value

                # Put item to DynamoDB table
                batch.put_item(Item=item)
                print(f"Successfully added item: {item}")

    return "Successfully processed data from Kinesis stream."
