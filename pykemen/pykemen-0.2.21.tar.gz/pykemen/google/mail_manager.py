"""Mail Manager module.

This module have a class with all needed functionalites
of Mail that AudienceScore needs.
"""
__author__ = 'Metriplica-Ayyoub&Javier'

import base64
from pykemen import utilities
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from apiclient import errors  # noqa


class Mail(object):
    """Mail class.

    Useful to send messages form the specified account.
    """

    def __init__(self, secrets, credentials):
        """Init module initialize and create Mail class.

        Args:
            credentials (str): Credentials to access to the client services
            secrets (str): Secrets of the Google accout to use

        Returns:
            Mail: with given configuration.
        """
        scopes = ["https://www.googleapis.com/auth/gmail.send"]
        self._gmail_service = utilities.create_api('gmail', 'v1', scopes, secrets, credentials)

    def _create_message(self, frm, to, subject, body, type='plain'):
        """Create a message object."""
        if type == "MimeType":
            message = body
        else:
            message = MIMEText(body, type)
        message['bcc'] = ','.join(to)
        message['from'] = frm
        message['subject'] = subject
        return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode("utf8"), 'payload': {'mimeType': 'text/html'}}

    def send_message(self, frm, to, subject,  message, type):
        """Send a message to specified reciver.

        Args:
            to (list): Recivers of the email separated by comma
            subject (str): subject of the email
            message (str|MimeMultipart): message or body of the email

        Returns:
            int: message id.

        """
        try:
            object_message = self._create_message(frm, to, subject, message, type)
            messageId = self._gmail_service.users().messages().send(
                userId='me', body=object_message).execute()
            return messageId
        except errors.HttpError as error:
            raise Exception(error)


    def create_multipart_email(self, config):

        html_part = MIMEMultipart()

        for element in config:
            if element.get("kind") == "image":
                img_data = open(element.get("filename"), "rb").read()
                img = MIMEImage(img_data, element.get("subtype"))
                img.add_header("Content-Id", f"<{element.get('id')}>")
                img.add_header("Content-Disposition", element.get("disposition", "inline") , filename=element.get("filename"))
                html_part.attach(img)
            
            if element.get("kind") == "html":
                html = open(element.get("filename"), "r").read()
                for key in element.get("kwargs", {}).keys():
                    html = html.replace("{"+str(key)+"}", str(element.get("kwargs").get(key)))
                html_part.attach(MIMEText(html, _subtype="html"))
            if element.get("kind")=="plain":
                plain = MIMEText(element.get("message"), _subtype=element.get("kind"))
                html_part.attach(plain)
        
        return html_part