# Serverless Emailing using AWS

this project can be used to send emails to senders using AWS. This is better than a normal email since we can schedule or trigger emails according to our demand. We have to keep in mind that the two tools that are used in this project are Amazon Simple Emailing Service (SES) and AWS Lambda.

## Steps of implementation
- First create a Lambda function and select Python 3.8 in the Runtime menu. 
- Now we will have to create a new permission for our lambda function to access SES. To do this go to configuration tab in the lambda function and go to premissions. We can see that a default role is created for the function called "ses-email-role-u412n10d". Click on this role and we will be redirected to a new IAM Console page.
![App Page](https://github.com/anshulsathe/Serverless-Emailing-Using-AWS/blob/main/Screenshot%20(128).png)
- In the IAM Console, we can see that we have a permission policy given. We have to create a new inline policy under the add permissions tab. 
- In the visual editor for the inline policy tab, we have to select all write premissions under the write tab in the SES Service. Now select "All Resource" under the resource tab. Now we can click on review policy and create permission.

This concludes one part of our project, we have succesfully given our lambda function "ses-email" permissions to write emails by accessing SES. Now we will be configuring SES.

- In SES, click on the create identity option. Here select "email address" and write your email address. An email will be sent to this address in order to confirm and verify your identity.
- After this is done, write the following code in your "ses-emailing" lambda function:
```bash
import json
import boto3

def lambda_handler(event, context):
    sesClient = boto3.client("ses", region_name="your-region")
    
    emailResponse = sesClient.send_email(
        Destination={
            "ToAddresses" : [
                "receiver1@mail", "receiver2@mail.com"
            ],
        },
        Message={
            "Body": {
                "Text": {
                    "Data" : "Succesfully sent and email using SES"
                }
            },
            "Subject" :{
                "Data" : "AWS Project TEST"
            },
        },
        Source="sender@mail.com"
        )
```
After deploying this code, we can click on test. An test email will be sent on the selected destination mail ids. Thank you for reading.
![App Page](https://github.com/anshulsathe/Serverless-Emailing-Using-AWS/blob/main/Screenshot%20(129).png)
