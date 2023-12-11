import base64
import json
from datetime import datetime


def lambda_handler(event, context):
    """
    This Lambda function processes incoming base64-encoded JSON data and adds a new key-value pair before returning the data.
    """

    output_records = []

    # Loop through each record in the event
    for record in event["records"]:

        # Extract the message and decode it from base64 and UTF-8
        message = base64.b64decode(record["data"]).decode("UTF-8")

        # Parse the message as JSON
        data = json.loads(message)

        # Add a new key-value pair
        data["l3"] = 19

        # Encode the updated data back to JSON and then base64
        output_data = base64.b64encode(bytes(json.dumps(data), "utf-8"))

        # Construct and append the output record
        output_record = {
            "recordId": record["recordId"],
            "result": "Ok",
            "data": output_data,
        }
        output_records.append(output_record)

    # Return the output with the processed records
    return {"records": output_records}
