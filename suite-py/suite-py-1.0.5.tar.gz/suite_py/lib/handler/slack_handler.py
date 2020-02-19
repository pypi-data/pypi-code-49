# -*- encoding: utf-8 -*-
import slack

from suite_py.lib.tokens import Tokens
from suite_py.lib.singleton import Singleton

tokens = Tokens()


class SlackHandler(metaclass=Singleton):
    _client = None

    def __init__(self):
        self._client = slack.WebClient(token=tokens.slack)

    def post(self, channel, text):
        self._client.chat_postMessage(channel=channel, text=text, as_user=True)
