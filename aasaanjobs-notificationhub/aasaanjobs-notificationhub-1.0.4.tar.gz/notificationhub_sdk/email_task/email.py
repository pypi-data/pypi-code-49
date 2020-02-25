import json
from typing import List

from ..base import get_expiry, validate_email, validate_template, validate_attachment_url
from ..common import Waterfall, Platform
from ..proto import notification_hub_pb2 as pb


class EmailRecipient:

    def __init__(self, email: str, name: str = "", user_id: str = ""):
        """
        Parameters:
            email (str): Email ID
            name (str, optional): The name of the person or company
            user_id (str, optional): The User ID to whom the notification is being sent
        """
        self._email_recipient = pb.EmailRecipient()
        validate_email(email)
        self._email_recipient.email = email
        self._email_recipient.name = name
        self._email_recipient.userID = user_id if user_id else ''

    @property
    def proto(self) -> pb.EmailRecipient:
        return self._email_recipient


class EmailAttachment:

    def __init__(self, file_name: str, url: str):
        """
        Parameters:
            file_name (str): The filename of the attachment
            url (str): Accessible URL of the file
        """
        validate_attachment_url(url)
        self._email_attachment = pb.EmailAttachment()
        self._email_attachment.filename = file_name
        self._email_attachment.url = url

    @property
    def proto(self) -> pb.EmailAttachment:
        return self._email_attachment


class Email:
    _default_expiry_offset = 7    # 7 Days

    def __init__(
            self,
            send_to: List[EmailRecipient],
            template: str,
            subject: str,
            context: dict = None,
            sender: EmailRecipient = None,
            reply_to: EmailRecipient = None,
            cc: List[EmailRecipient] = None,
            attachments: List[EmailAttachment] = None,
            waterfall_config: Waterfall = None,
            expiry: int = None,
            platform: Platform = Platform.Aasaanjobs
    ):
        """
        Parameters:
            send_to (EmailRecipient[]): An array of recipients. Each object within this array may contain the name,
                but must always contain the email, of a recipient. (min: 1, max: 1000)
            template (str): The Email base template URL which will get rendered with the variable data provided.
            subject (str): The subject of your email. Char length requirements, according to the RFC -
                http://stackoverflow.com/questions/1592291/what-is-the-email-subject-length-limit#answer-1592310
            context (dict, optional): A dictionary of variable data to be rendered in the template
            sender (EmailRecipient, optional): The name and email of the person who is sending the mail
            reply_to (EmailRecipient, optional): The name and email of the person to whom recipients can reply to
            cc (EmailRecipient[], optional): An array of recipients who will receive a copy of your email. Each object
                within this array may contain the name, but must always contain the email, of a recipient.
            attachments (EmailAttachment[], optional): An array of objects in which you can specify any attachments
                you want to include.
            waterfall_config (Waterfall, optional): The configuration to be used by Hub priority engine to schedule
                this channel
            expiry (int, optional): The Epoch timestamp at which this notification task should expire if still not sent
        """
        self._email = pb.Email()
        self.__set_recipients(send_to)

        validate_template(template)
        self._email.template = template

        self._email.subject = subject
        self.platform = platform
        self._email.context = json.dumps(context) if context else '{}'
        self.__set_attachments(attachments)
        self._email.sender.CopyFrom(self.__set_sender(sender))
        self._email.replyTo.CopyFrom(self.__set_reply_to(reply_to))
        self.__set_cc(cc)
        self.__set_waterfall(waterfall_config)
        self._email.expiry = expiry if expiry else get_expiry(self._default_expiry_offset)

    def __set_recipients(self, send_to: List[EmailRecipient]):
        for _ in send_to:
            self._email.toRecipients.append(_.proto)

    def __set_cc(self, cc: List[EmailRecipient]):
        if not cc:
            cc = []
        for _ in cc:
            self._email.ccRecipients.append(_.proto)

    def __set_attachments(self, attachments: List[EmailAttachment]):
        if not attachments:
            attachments = []
        for _ in attachments:
            self._email.attachments.append(_.proto)

    def __set_sender(self, sender: EmailRecipient = None):
        if sender:
            return sender.proto
        if self.platform == Platform.Aasaanjobs:
            return EmailRecipient('noreply@aasaanjobs.com', 'Aasaanjobs').proto
        else:
            return EmailRecipient('noreply@olxpeople.com', 'OLX People').proto

    def __set_reply_to(self, reply_to: EmailRecipient = None):
        if reply_to:
            return reply_to.proto
        if self.platform == Platform.Aasaanjobs:
            return EmailRecipient('support@aasaanjobs.com', 'Aasaanjobs').proto
        else:
            return EmailRecipient('support@olxpeople.com', 'OLX People').proto

    def __set_waterfall(self, value: Waterfall = None):
        if not value:
            value = Waterfall()
        self._email.waterfallConfig.CopyFrom(value.proto)

    @property
    def proto(self) -> pb.Email:
        return self._email
