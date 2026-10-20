# AWS repo
This project contains a collection of AWS scripts. 

DirName      | Description
------------- | -------------  
digrams | Solutions architect diagrams
iam/policies | iam/s3 policy templates

## Lambda deployment
All Lambdas are Python files with a `lambda_handler(event, context)` function, so the handler is `<file name without .py>.lambda_handler`. The code does not pin a runtime version; choose a Python runtime that includes `boto3`. Only the environment variables listed below are read by the code. Anything else is hard-coded and must be edited in the file before deploying.

File | Trigger | Environment variables read | Hard-coded values to change
------------- | ------------- | ------------- | -------------
kinesis-event-to-s3.py | Kinesis stream | `BUCKET_NAME` (default `kotharv-target`) | Writes each invocation to `kinesis/<timestamp>-<request id>.txt`
s3-csv-to-dynamo.py | Kinesis stream (CSV payloads with a header row) | `AWS_REGION` (set by Lambda; default `us-east-1`) | DynamoDB table `my_table`; `my_id` is stored as a number
s3-event-to-kinesis.py | S3 object-created event | none | Kinesis stream `my_stream_name`, partition key `my_partition_key`
transform-record.py | Firehose data transformation (`records` key) | none | Adds `l3 = 19` to each JSON record; failed records return `ProcessingFailed`

Permissions needed by each execution role:
- kinesis-event-to-s3.py: `s3:PutObject` on the target bucket.
- s3-csv-to-dynamo.py: the Kinesis read permissions for the event source (`kinesis:GetRecords`, `kinesis:GetShardIterator`, `kinesis:DescribeStream`) and `dynamodb:BatchWriteItem` on `my_table`.
- s3-event-to-kinesis.py: `s3:GetObject` on the source bucket and `kinesis:PutRecord` on the stream.
- transform-record.py: no AWS API calls; it needs only basic Lambda logging.

