import json
import boto3


def lambda_handler(event, context):
    sesClient = boto3.client("ses", region_name="your-region")

    emailResponse = sesClient.send_email(
        Destination={
            "ToAddresses": [
                "receiver1@mail", "receiver2@mail.com"
            ],
        },
        Message={
            "Body": {
                "Text": {
                    "Data": "Succesfully sent and email using SES"
                }
            },
            "Subject": {
                "Data": "AWS Project TEST"
            },
        },
        Source="sender@mail.com"
    )