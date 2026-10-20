import base64
import os
from datetime import datetime, timezone

import boto3


# The bucket name is read from the BUCKET_NAME environment variable. The
# previously hard-coded value is kept as the fallback so existing deployments
# that do not set the variable keep working.
bucket_name = os.environ.get("BUCKET_NAME", "kotharv-target")

s3_client = boto3.client("s3")


def lambda_handler(event, context):

    # Create an empty list to store the decoded payloads
    payloads = []

    # Iterate through each record in the event
    for record in event['Records']:

        # Decode the base64 encoded Kinesis data and keep the raw payload bytes
        payloads.append(base64.b64decode(record["kinesis"]["data"]))

    # One object per invocation. The key combines a UTC timestamp with the
    # request ID so concurrent or repeated invocations never overwrite each other.
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    request_id = getattr(context, "aws_request_id", "local")
    object_key = f"kinesis/{timestamp}-{request_id}.txt"

    # Write the decoded payloads, one per line
    body = b"\n".join(payloads) + b"\n"

    # Upload the event data to the S3 bucket
    s3_client.put_object(Body=body, Bucket=bucket_name, Key=object_key)

    return "Successfully uploaded data to S3 bucket."
