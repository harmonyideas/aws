import boto3
import json
import base64

# Accessing resources
s3 = boto3.resource('s3', region_name='<>')
dynamodb = boto3.resource('dynamodb', region_name='<>')
table = dynamodb.Table('my_table')

def lambda_handler(event, context):
    # Decode Kinesis data
    for record in event['Records']:
        payload = base64.b64decode(record['kinesis']['data']).decode()

    # Process data from CSV file
    data_list = payload.split('\r\n')
    keys = data_list[0].split(',')

    for record in data_list[1:-1]:
        values = record.split(',')
        item = {}
        
        # Handle missing values
        for i, value in enumerate(values):
            if not value:
                value = 'default_value'
            key = keys[i]
            item[key] = int(value) if key == 'my_id' else value

        # Put item to DynamoDB table
        table.put_item(Item=item)
        print(f"Successfully added item: {item}")

    return "Successfully processed data from Kinesis stream."
