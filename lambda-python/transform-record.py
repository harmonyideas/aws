import base64
import json


def lambda_handler(event, context):
    """
    This Lambda function processes incoming base64-encoded JSON data and adds a new key-value pair before returning the data.
    Records that cannot be decoded or parsed are returned as "ProcessingFailed" with their original data.
    """

    output_records = []

    # Loop through each record in the event
    for record in event["records"]:
        record_id = record["recordId"]

        try:
            # Extract the message and decode it from base64 and UTF-8
            message = base64.b64decode(record["data"]).decode("UTF-8")

            # Parse the message as JSON
            data = json.loads(message)

            # Add a new key-value pair
            data["l3"] = 19

            # Encode the updated data back to JSON and then base64.
            # b64encode returns bytes, so decode to str for the Firehose response.
            output_data = base64.b64encode(json.dumps(data).encode("UTF-8")).decode("UTF-8")

            output_records.append({
                "recordId": record_id,
                "result": "Ok",
                "data": output_data,
            })
        except (ValueError, TypeError) as exc:
            # Covers bad base64, bad UTF-8, invalid JSON, and non-object JSON.
            # Firehose sends the original data back so the failure can be
            # routed to the error prefix.
            print(f"Failed to process record {record_id}: {exc}")
            output_records.append({
                "recordId": record_id,
                "result": "ProcessingFailed",
                "data": record["data"],
            })

    # Return the output with the processed records
    return {"records": output_records}
