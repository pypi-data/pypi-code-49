import importlib
import os

import boto3

from notificationhub_sdk.base import ImproperlyConfigured


class SQSProducer:
    """
    Used for pushing the messages to SQS
    """
    setting_keys = (
        ('access_key_id', 'NOTIFICATION_HUB_SQS_ACCESS_KEY_ID'),
        ('secret_access_key', 'NOTIFICATION_HUB_SQS_SECRET_ACCESS_KEY'),
        ('region', 'NOTIFICATION_HUB_SQS_REGION'),
        ('queue_name', 'NOTIFICATION_HUB_SQS_QUEUE_NAME')
    )

    def __init__(self, **kwargs):
        # Retrieve Settings
        self.access_key_id = self._get_setting(*self.setting_keys[0], **kwargs)
        self.secret_access_key = self._get_setting(*self.setting_keys[1], **kwargs)
        self.region = self._get_setting(*self.setting_keys[2], **kwargs)
        self.queue_name = self._get_setting(*self.setting_keys[3], **kwargs)

        self._session = None
        self._queue = None
        self.init_sqs_session(kwargs.get('endpoint_url'))

    def _get_setting(self, kw_name, env_name, **kwargs):
        if kwargs.get(kw_name):
            return kwargs[kw_name]
        value = self.__get_from_django_settings(env_name)
        # If not found in Django settings, retrieve from environment variables
        if not value:
            value = os.getenv(env_name)
        # Throw error if still failed to retrieve the setting
        if not value:
            raise ImproperlyConfigured('Missing required settings `{}`'.format(env_name))
        return value

    @staticmethod
    def __get_from_django_settings(name):
        """
        If the Django project is initiated, then retrieves the settings
        from Django settings
        :param name: Setting Name
        :return: Setting Value
        """
        try:
            module = importlib.import_module('django.conf')
            settings = getattr(module, 'settings')
            return getattr(settings, name, None)
        except ImportError:
            return None

    def init_sqs_session(self, endpoint_url=None):
        """
        Initiates SQS session
        """
        client_kwargs = {
            'service_name': "sqs",
            'aws_access_key_id': self.access_key_id,
            'aws_secret_access_key': self.secret_access_key,
            'region_name': self.region
        }
        if endpoint_url:
            client_kwargs['endpoint_url'] = endpoint_url
        self._session = boto3.resource(**client_kwargs)
        self._queue = self._session.get_queue_by_name(QueueName=self.queue_name)

    def send_message(self, message_body: str) -> str:
        """
        Sends a message to Amazon SQS
        :param message_body: The message to be pushed to queue
        :returns The MessageId returned by AWS
        :raises ConnectionError if failure in sending occurs
        """
        res = self._queue.send_message(QueueUrl=self._queue.url, MessageBody=str(message_body))
        status_code = res.get('ResponseMetadata').get('HTTPStatusCode')
        if status_code / 100 != 2:
            raise ConnectionError('Failed to send message to Hub Queue')
        return res['MessageId']
