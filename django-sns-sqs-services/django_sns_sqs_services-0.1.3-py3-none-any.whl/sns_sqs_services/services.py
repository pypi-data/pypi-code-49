import boto3
from django.conf import settings
import json
from rest_framework.utils.encoders import JSONEncoder

"""
Description: Class helper for messages sns, sqs AWS
"""

class SqsService:
    """
    Function to send message to sqs
    Params: queue_name, msg
    """
    def push(self, queue_name, msg, base_url=None):
        try:
            if settings.ENVIRONMENT == 'LOCAL':
                base_url = settings.AWS_SQS_URL
        except Exception:
            pass

        sqs = boto3.resource('sqs',
                             endpoint_url=base_url,
                             region_name=settings.AWS_REGION_NAME,
                             aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                             aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)

        queue = sqs.get_queue_by_name(QueueName=queue_name)

        try:
            queue.send_message(MessageBody=json.dumps(msg, cls=JSONEncoder))
            return True
        except Exception:
            raise ValueError('Could not send message to SQS')


class SnsService:
    """
    Function to send message to topic sns
    Params: arn, atrribute, msg
    """
    def push(self, arn=None, attribute=None, msg=None, base_url=None):
        try:
            if settings.ENVIRONMENT == 'LOCAL':
                base_url = settings.AWS_SNS_URL
        except Exception:
            pass

        sns = boto3.client('sns',
                           endpoint_url=base_url,
                           region_name=settings.AWS_REGION_NAME,
                           aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                           aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)

        try:
            if not attribute:
                attribute = self.make_attributes()

            sns.publish(TopicArn=arn,
                        Message=json.dumps(msg, cls=JSONEncoder),
                        MessageAttributes=attribute)
            return True

        except Exception:
            raise ValueError('Could not send message to SNS')

    """
    Function to make an object attribute
    Params: entity, type, status, event
    """
    def make_attributes(self, entity=None, type=None, status=None, event=None):

        attributes = {}
        try:
            if settings.ENVIRONMENT:
                attributes['environment'] = {
                    "DataType": "String",
                    "StringValue": settings.ENVIRONMENT
                }

            if settings.COUNTRY_PREFIX:
                attributes['country_prefix'] = {
                    "DataType": "String",
                    "StringValue": settings.COUNTRY_PREFIX
                }
        except Exception:
            print('Environment Vars not present')

        if entity:
            attributes["entity"] = {
                "DataType": "String",
                "StringValue": entity
            }
        if type:
            attributes["type"] = {
                "DataType": "String",
                "StringValue": type
            }
        if status:
            attributes["status"] = {
                "DataType": "String",
                "StringValue": status
            }
        if event:
            attributes["event"] = {
                "DataType": "String",
                "StringValue": event
            }
        return attributes

    """
    Function to get complete string arn by topic name
    Params: name (topic name)
    """
    def get_arn_by_name(self, name, base_url=None):
        try:
            if settings.ENVIRONMENT == 'LOCAL':
                base_url = settings.AWS_SNS_URL
        except:
            pass

        sns = boto3.client('sns',
                           endpoint_url=base_url,
                           region_name=settings.AWS_REGION_NAME,
                           aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                           aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)

        for arn in sns.list_topics()['Topics']:
            if arn['TopicArn'].split(':')[5] == name:
                return arn['TopicArn']

        raise Exception("Topic Not Found")
