import boto3
import json
import logging
import os

from base64 import b64decode
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError


# The base-64 encoded, encrypted key (CiphertextBlob) stored in the kmsEncryptedHookUrl environment variable
ENCRYPTED_HOOK_URL = os.environ['kmsEncryptedHookUrl']
# The Slack channel to send a message to stored in the slackChannel environment variable
SLACK_CHANNEL = os.environ['slackChannel']

HOOK_URL = "https://" + boto3.client('kms').decrypt(
   CiphertextBlob=b64decode(ENCRYPTED_HOOK_URL),
   EncryptionContext={'LambdaFunctionName': os.environ['AWS_LAMBDA_FUNCTION_NAME']}
)['Plaintext'].decode('utf-8')


logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    logger.info("Event: " + str(event))
    message = event['Records'][0]['Sns']['Message']
    logger.info("Message: " + str(message))

    slack_message = {
        'channel': SLACK_CHANNEL,
        'username' : 'AWS',
        'icon_emoji' : ':aws:',
        'attachments' : [
            {
                'color' : 'FF0000',
                "blocks": [
            		{
            			"type": "header",
            			"text": {
            				"type": "plain_text",
            				"text": 'DevOps Guru for ' + message['Anomalies'][0]['SourceDetails'][0]['DataIdentifiers']['ResourceType']
            			}
            		},
            		{
    					"type": "divider"
    				},
        			{
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "*Insight Name:* " + message['InsightName']
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "*Insight Type:* " + message['InsightType']
                        }
                    },
                    {
                        "type": "section",
                        "fields": [
                            {
                                "type": "mrkdwn",
                                "text": "*Insight Severity:* " + message['InsightSeverity']
                            },
                            {
                                "type": "mrkdwn",
                                "text": "*Link:* <" + message['InsightUrl'] + "| AWS DevOps Guru>"
                            }
                        ]
                    },
    			]
            }
        ]
    }

    req = Request(HOOK_URL, json.dumps(slack_message).encode('utf-8'))
    try:
        response = urlopen(req)
        response.read()
        logger.info("Message posted to %s", slack_message['channel'])
    except HTTPError as e:
        logger.error("Request failed: %d %s", e.code, e.reason)
    except URLError as e:
        logger.error("Server connection failed: %s", e.reason)
