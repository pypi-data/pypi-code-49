from datetime import datetime
from typing import Tuple

from ..proto import notification_hub_pb2 as pb

from ..common import Platform
from ..email_task import Email
from ..sms import Sms
from ..whatsapp import Whatsapp
from ..mobile_push import Push
from ..common import WaterfallMode, MessageType
from ..sqs import SQSProducer
import uuid
import os


class Task:
    """
    A wrapper class for NotificationTask protobuf structure
    """

    def __init__(self, name: str, sent_by_id: str, client: str, platform: Platform,
                 message_type: MessageType = MessageType.MARKETING, email: Email = None, sms: Sms = None,
                 whatsapp: Whatsapp = None, push: Push = None, waterfall_type: WaterfallMode = WaterfallMode.AUTO):
        """
        Parameters:
            name (str): A unique name for this notification task
            sent_by_id (str): ID of the user who triggered the notification
            client (str): Name of the application or service triggering the notification
            platform (Platform): Which company vertical are we sending from
            message_type (MessageType, optional): Medium of the notifications (defaults to MessageType.MARKETING)
            email (Email, optional): The Email object (refer Email docs)
            sms (Sms, optional): The SMS object (refer SMS docs)
            whatsapp (Whatsapp, optional): The WhatsApp object  (refer WhatsApp docs)
            push (Push, optional): The Push object (refer Push docs)
            waterfall_type (WaterfallMode, optional): Whether to override the default priority engine logic or not
        """
        self._task = pb.NotificationTask()

        # Check whether at least one channel is specified
        if not email and not sms and not whatsapp and not push:
            raise AssertionError('At least one channel should be passed')
        self.__set_id()
        self.__set_triggered_on()

        self._task.name = name
        self._task.sentByID = sent_by_id
        self._task.client = client
        self._task.platform = platform
        self._task.messageType = message_type
        self._task.waterfallType = waterfall_type

        # Assign the notification channels
        self.__set_sms(sms)
        self.__set_email(email)
        self.__set_whatsapp(whatsapp)
        self.__set_push(push)

    def __set_id(self):
        """
        Generates a UUID v4 and assigns the value as ID
        """
        self._task.ID = str(uuid.uuid4())

    def __set_triggered_on(self):
        """
        Sets the current timestamp as triggered on
        """
        now = datetime.now()
        self._task.triggeredOn = int(datetime.timestamp(now))

    def __set_sms(self, value: Sms):
        if not value:
            return
        self._task.sms.CopyFrom(value.proto)

    def __set_email(self, value: Email):
        if not value:
            return
        # Set the platform
        value.platform = self._task.platform
        self._task.email.CopyFrom(value.proto)

    def __set_whatsapp(self, value: Whatsapp):
        if not value:
            return
        self._task.whatsapp.CopyFrom(value.proto)

    def __set_push(self, value: Push):
        if not value:
            return
        self._task.push.CopyFrom(value.proto)

    @property
    def proto(self) -> pb.NotificationTask:
        return self._task

    def send(self, **kwargs) -> Tuple[str, str]:
        """
        Sends the notification task to Notification Hub Queue
        :returns: The Task ID and the AWS Message ID.
        """

        if self._task.messageType == MessageType.MARKETING:
            queue_name = os.getenv('NOTIFICATION_HUB_MARKETING_SQS_QUEUE_NAME')
        elif self._task.messageType == MessageType.TRANSACTIONAL:
            queue_name = os.getenv('NOTIFICATION_HUB_SQS_QUEUE_NAME')

        kwargs.update({"queue_name": queue_name})

        producer = SQSProducer(**kwargs)
        aws_msg_id = producer.send_message(self._task)
        return self._task.ID, aws_msg_id
