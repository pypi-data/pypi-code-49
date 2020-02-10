from __future__ import print_function, unicode_literals
from ..tokens import Tokens
from ..config import Config
from ..singleton import Singleton
from PyInquirer import prompt
import slack

import os

tokens = Tokens()


class SlackHandler(metaclass=Singleton):
    _client = None

    def __init__(self):
        self._client = slack.WebClient(token=tokens.slack)

    def post(self, channel, text):
        self._client.chat_postMessage(
            channel=channel,
            text=text,
            as_user=True
        )
