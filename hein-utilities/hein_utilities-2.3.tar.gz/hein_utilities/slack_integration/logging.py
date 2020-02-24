from typing import Union, List
from logging import StreamHandler, LogRecord, Formatter
from .bots import SlackBot, RTMSlackBot


# some predefined formatters for convenience
# detailed message with time, name, level, and message
DETAILED_FORMATTER = Formatter(
    '`%(asctime)s` `%(name)s` *%(levelname)s*: %(message)s'
)

# timestamped message
TIMESTAMPED_FORMATTER = Formatter(
    '`%(asctime)s` %(message)s'
)


class SlackLoggingHandler(StreamHandler):
    # default formatter
    DEFAULT_FORMATTER = TIMESTAMPED_FORMATTER

    def __init__(self,
                 token: str,
                 channel_name: str,
                 user_member_ids: Union[str, List[str]] = None,
                 alert_level: int = 30,
                 formatter: Formatter = None,
                 **kwargs,
                 ):
        """
        A logging stream handler which logs to a slack channel. This class encompasses the RTMSlackBot class to enable
        real-time-messaging handling using the connected slack bot.

        :param str token: token to connect to slack client
        :param str channel_name: channel to message on. for example, #channelname
        :param user_member_ids: user member ID(s) to tag if something goes wrong (if logging level exceeds alert level)
        :param alert_level: alert level to notify the defined user at
        :param formatter: logging formatter to use (if not specified, the class DEFAULT_FORMATTER is used)
        """
        StreamHandler.__init__(self)
        if formatter is None:
            formatter = self.DEFAULT_FORMATTER
        self.setFormatter(formatter)
        self.alert_level = alert_level
        self.bot = SlackBot(
            user_member_ids=user_member_ids,
            token=token,
            channel_name=channel_name,
            **kwargs,
        )

    def emit(self, record: LogRecord) -> None:
        # catch and format message
        msg = self.format(record)
        # determine whether to tag admin
        tag_admin = True if record.levelno >= self.alert_level else False
        self.bot.post_slack_message(
            msg,
            tag_admin=tag_admin,
        )


class RTMSlackLoggingHandler(StreamHandler):
    # default formater
    DEFAULT_FORMATTER = TIMESTAMPED_FORMATTER

    def __init__(self,
                 token: str,
                 channel_name: str,
                 user_member_ids: Union[str, List[str]] = None,
                 alert_level: int = 30,
                 formatter: Formatter = None,
                 **kwargs,
                 ):
        """
        A logging stream handler which logs to a slack channel. This class encompasses the RTMSlackBot class to enable
        real-time-messaging handling using the connected slack bot.

        :param str token: token to connect to slack client
        :param bot_name: name for the bot
        :param str channel_name: channel to message on. for example, #channelname
        :param user_member_ids: user member ID(s) to tag if something goes wrong (if logging level exceeds alert level)
        :param alert_level: alert level to notify the defined user at
        """
        StreamHandler.__init__(self)
        if formatter is None:
            formatter = self.DEFAULT_FORMATTER
        self.setFormatter(formatter)
        self.alert_level = alert_level
        self.bot = RTMSlackBot(
            user_member_ids=user_member_ids,
            token=token,
            channel_name=channel_name,
            **kwargs,
        )

    def emit(self, record: LogRecord) -> None:
        # catch and format message
        msg = self.format(record)
        # determine whether to tag admin
        tag_admin = True if record.levelno >= self.alert_level else False
        self.bot.post_slack_message(
            msg,
            tag_admin=tag_admin,
        )

    def run_on(self, *, event: str):
        """a pass-through for the RTMClient.run_on decorator"""
        return self.bot.rtm_client.run_on(event=event)

    def start_rtm_thread(self):
        """starts the RTM monitor thread"""
        self.bot.start_rtm_client()
