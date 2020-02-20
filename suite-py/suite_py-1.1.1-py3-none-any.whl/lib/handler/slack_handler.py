# -*- encoding: utf-8 -*-
import slack

from suite_py.lib.tokens import Tokens
from suite_py.lib.singleton import Singleton
from suite_py.lib.logger import Logger
from suite_py.lib.config import Config

tokens = Tokens()
config = Config().load()
logger = Logger()


class SlackHandler(metaclass=Singleton):
    _client = None

    def __init__(self):
        self._client = slack.WebClient(token=tokens.slack)

    def post(self, channel_config, text):
        channel = config["user"].get(channel_config)
        if channel:
            try:
                self._client.chat_postMessage(channel=channel, text=text, as_user=True)
            except Exception:
                logger.warning("Non sono riuscito a inviare il messaggo su Slack")
        else:
            logger.info("Le notifiche su Slack sono disabilitate")
