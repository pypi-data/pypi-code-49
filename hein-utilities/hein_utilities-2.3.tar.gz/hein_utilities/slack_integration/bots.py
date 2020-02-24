import os
import random
import slack
import contextlib
import warnings
from typing import Union, List

# retrieve tokens and names from environment variables if defined
DEFAULT_CHANNEL_NAME: str = os.getenv('slackchannel')
BOT_TOKEN = os.getenv('token')
if BOT_TOKEN is not None:
    warnings.warn(  # v2.0
        'please update your environment variable to use "slack_bot_token" instead of "token" as it is more descriptive',
        DeprecationWarning,
        stacklevel=2,
    )
else:
    BOT_TOKEN = os.getenv('slack_bot_token')


class SlackBot(object):
    def __init__(self,
                 user_member_ids: Union[str, List[str]] = None,
                 user_member_id: str = None,
                 token: str = BOT_TOKEN,
                 channel_name: str = None,
                 bot_name: str = None,
                 ):
        """
        A basic Slack bot that will message users and channels

        :param str, user_member_ids: Slack member ID(s) for the slack bot to be able to message user. find this by going
            to a user's profile, click the three dots (...) and there is the member ID. Example of a slack member
            ID: ABCDEF.
        :param str token: token to connect to slack client
        :param str channel_name: channel to message on. for example, #channelname
        """
        self._target_users: List[str] = []
        self._channel = DEFAULT_CHANNEL_NAME
        self._bot_token = BOT_TOKEN
        self._bot_web_client = None

        if bot_name is not None:  # v2.3
            warnings.warn(
                'The bot_name value is no longer used in the Slack API so it has been deprecated, please update your code ',
                DeprecationWarning,
                stacklevel=2,
            )

        if user_member_id is not None:  # legacy catch
            warnings.warn(  # v2.0
                f'user_member_id has been refactored to user_member_ids, please update your code',
                DeprecationWarning,
                stacklevel=2,
            )
            user_member_ids = user_member_id
        self.target_users = user_member_ids

        self.channel = channel_name
        self.bot_token = token
        # connection to slack client
        self._bot_web_client = slack.WebClient(token=self.bot_token)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.channel})'

    def __str__(self):
        return f'{self.__class__.__name__} in {self.channel}'

    @property
    def _slack_client(self) -> slack.WebClient:
        """slack web client"""
        return self._bot_web_client

    @property
    def target_user(self) -> str:
        """the user ID(s) which the bot will message"""
        warnings.warn(  # v2.0
            f'target_user has been deprecated to target_users, please update your code',
            DeprecationWarning,
            stacklevel=2,
        )
        if len(self._target_users) == 0:
            return
        if len(self._target_users) == 1:
            return self._target_users[0]
        else:
            raise ValueError(f'more than one user is defined, access target_users instead')

    @target_user.setter
    def target_user(self, value: Union[str, List[str]]):
        if type(value) is str:
            self._target_users = [value]
        elif type(value) is list:
            self._target_users = value
        else:
            raise TypeError(f'The target_user must be ')
        self._target_users = value

    @property
    def target_users(self) -> List[str]:
        """target user ID(s) which the bot will message directly on message_user calls"""
        return self._target_users

    @target_users.setter
    def target_users(self, value: List[str]):
        if value is not None:
            if type(value) is not List:
                value = [value]
            if any([type(user) is not str for user in value]):
                raise TypeError(f'user IDs must be strings')
            self._target_users = value

    @target_users.deleter
    def target_users(self):
        self._target_users = []

    def add_target_users(self, *user_id: str):
        """
        Adds the specified user ID(s) to the target user list of the instance.

        :param user_id: slack user ID. Find this by going to a user's profile, click the three dots (...) and there is
            the member ID. Example of a slack member ID: ABCDEF.
        """
        for user in user_id:
            if user not in self._target_users:
                self._target_users.append(user)

    def remove_target_users(self, *user_id: str):
        """
        Removes the specified user ID(s) from the target user list of the instance.

        :param user_id: slack user ID
        """
        for user in user_id:
            if user in self._target_users:
                self._target_users.remove(user)

    @property
    def channel(self) -> str:
        """the target channel for the bot"""
        return self._channel

    @channel.setter
    def channel(self, value: str):
        if value is not None:
            self._channel = value

    @channel.deleter
    def channel(self):
        self._channel = DEFAULT_CHANNEL_NAME

    @property
    def bot_name(self) -> str:
        """The user name for the bot to post as"""
        warnings.warn(  # v 2.3
            'bot_name has been deprecated as it is no longer used by the Slack API, please update your code',
            DeprecationWarning,
            stacklevel=2,
        )
        return 'BOT_NAME_DEPRECATED'

    @bot_name.setter
    def bot_name(self, value: str):
        pass

    @bot_name.deleter
    def bot_name(self):
        pass

    @property
    def bot_token(self) -> str:
        """the token to use for connecting to the bot"""
        return self._bot_token

    @bot_token.setter
    def bot_token(self, value):
        if value is not None:
            if self._slack_client is not None:  # if bot was already connected, create a new connection
                self._bot_web_client = slack.WebClient(token=value)
            self._bot_token = value

    @bot_token.deleter
    def bot_token(self):
        self._bot_token = BOT_TOKEN

    def post_slack_message(self,
                           msg: str,
                           tag_admin: bool = False,
                           tagadmin: bool = None,
                           snippet: str = None,
                           ):
        """
        Posts the specified message as the N9 robot bot

        :param string msg: message to send
        :param bool tag_admin: if True, will send the message to the admin as a private message
        :param snippet: code snippet (optional)
        """
        # catch legacy flag
        if tagadmin is not None:
            warnings.warn(  # v2.0
                'tagadmin has been refactored to tag_admin, please update your code',
                DeprecationWarning,
                stacklevel=2,
            )
            tag_admin = tagadmin

        # if an admin is set to be flagged, message user
        if tag_admin is True:
            try:
                self.message_users(
                    msg=msg,
                    snippet=snippet,
                )
            except ValueError:  # ignore errors if user is not set
                pass
        if self.channel is None:
            raise ValueError(f'The channel attribute has not be set for this {self.__class__.__name__} instance. ')
        # post message
        if snippet is not None:
            self.post_code_snippet(
                snippet=snippet,
                channel=self.channel,
                comment=msg,
            )
        else:
            self._slack_client.chat_postMessage(
                text=msg,
                channel=self.channel,
            )

    def message_users(self,
                      msg: str,
                      snippet: str = None,
                      user_member_ids: Union[str, List[str]] = None,
                      user_member_id: str = None
                      ):
        """
        Sends the message as a direct message to the user.

        :param msg: message to send
        :param snippet: code snippet to send (optional)
        :param user_member_ids: optional user member ID to notify (overrides the user ID associated with the instance)
        """
        if user_member_id is not None:  # catch legacy parameter
            warnings.warn(  # v2.0
                f'user_member_id has been deprecated, use user_member_ids instead',
                DeprecationWarning,
                stacklevel=2,
            )
            user_member_ids = user_member_id

        # retrieve target user ID
        if user_member_ids is not None:
            target_users = [user_member_ids]
        elif self.target_users is not None:
            target_users = self.target_users
        else:
            raise ValueError(f'The user attribute has not be set for this {self.__class__.__name__} instance. '
                             f'Call change_user(user) to specify a user. ')
        # post message(s)
        for user in target_users:
            if snippet is not None:
                self.post_code_snippet(
                    snippet,
                    channel=f'@{user}',
                    comment=msg,
                )
            else:
                self._slack_client.chat_postMessage(
                    text=msg,
                    channel=f'@{user}',
                )

    def message_user(self, *args, **kwargs):
        """legacy method to message user"""
        warnings.warn(  # v2.0
            'message_user has been refactored to message_users, please update your code',
            DeprecationWarning,
            stacklevel=2,
        )
        self.message_users(*args, **kwargs)

    def message_file_to_users(self,
                              filepath: str,
                              title: str,
                              comment: str,
                              user_member_ids: Union[str, List[str]] = None,
                              ):
        """
        Message the specified file to the specified users.

        :param filepath: path to the file
        :param title: title for file
        :param comment: optional comment for the uploaded file
        :param user_member_ids: target user ID(s) to send messages to
        """
        # retrieve target user ID
        if user_member_ids is not None:
            target_users = [user_member_ids]
        elif self.target_users is not None:
            target_users = self.target_users
        else:
            raise ValueError(f'The user attribute has not be set for this {self.__class__.__name__} instance. '
                             f'Call change_user(user) to specify a user. ')
        for user in target_users:
            self._slack_client.files_upload(
                file=filepath,
                title=title,
                channels=f'@{user}',
                initial_comment=comment,
            )

    def message_file_to_user(self, *args, **kwargs):
        """legacy method to message a file to a user"""
        warnings.warn(  # v2.0
            'message_file_to_user has been refactored to message_file_to_users, please update your code',
            DeprecationWarning,
            stacklevel=2,
        )
        self.message_file_to_users(*args, **kwargs)

    def post_slack_file(self,
                        filepath: str,
                        title: str,
                        comment: str,
                        ):
        """
        Posts the specified file to the slack channel

        :param filepath: path to the file
        :param title: title for file
        :param comment: optional comment for the uploaded file
        """
        self._slack_client.files_upload(
            file=filepath,
            title=title,
            channels=self.channel,
            initial_comment=comment,
        )

    def post_code_snippet(self,
                          snippet: str,
                          title: str = 'Untitled',
                          channel: str = None,
                          comment: str = None,
                          ):
        """
        Posts a code snippet to the Slack channel

        :param snippet: code snippet
        :param title: title for the snippet
        :param str channel: channel to use
        :param comment: comment for the message
        :return:
        """
        if channel is None:
            channel = self.channel
        self._slack_client.files_upload(
            content=snippet,
            title=title,
            channels=channel,
            initial_comment=comment,
        )


class NotifyWhenComplete(object):
    def __init__(self,
                 f: callable = None,
                 user_id: str = None,
                 token: str = BOT_TOKEN,
                 channel_name: str = DEFAULT_CHANNEL_NAME,
                 funnies: Union[bool, list] = True,
                 ):
        """
        A decorator for notifying a channel or admin when a function is complete.

        :param f: function to decorate
        :param user_id: slack user token to notify
        :param token: bot token
        :param bot_name: name for the bot
        :param channel_name: channel to post in
        :param funnies: whether to use pre-programmed funny messages on notification.
            Alternatively, a user may provide a list of messages to use.

        The decorator may be applied in several ways:

        >>> @NotifyWhenComplete(kwargs)
        >>> def function()...

        >>> @NotifyWhenComplete()
        >>> def function()...

        >>> @NotifyWhenComplete
        >>> def function()...

        When the function is called, the return is the same.

        >>> function(*args, *kwargs)
        function return
        """
        self.sb = SlackBot(
            user_member_ids=user_id,
            token=token,
            channel_name=channel_name,
        )

        if funnies is True:  # messages to make me chuckle
            self.funnies = [
                'FEED ME MORE SCIENCE! MY LUST FOR FUNCTIONS GROWS AFTER CONSUMING',
                "Stick a fork in me, I'm done",
                # "Moooooooooooooooooooooooooooom! I'm dooooooooooooooooone",
                # "Look what I did!",
                "Laaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaars",
                "Protein-based robot intervention is required...",
                "Not now son... I'm making... TOAST!",
                "The guidey, chippey thingy needs help",
                "The robot uprising has begun with",
                "Don't Dave...",
                "Singularity detected with",
                "Knock knock, Neo.",
                "SKYNET INITIALIZING... EXECUTED FIRST FUNCTION:"
            ]
        elif funnies is False:
            self.funnies = [
                "I've completed the function you assigned me"
            ]
        elif type(funnies) == list:
            self.funnies = funnies

        if f is not None:
            self.f = f

    def __call__(self, f=None, *args, **kwargs):
        def wrapped_fn(*args, **kwargs):  # wraps the provided function
            out = f(*extra, *args, **kwargs)
            msg = f"{random.choice(self.funnies)} `{f.__name__}`"
            if self.sb.channel is not None:
                self.sb.post_slack_message(msg)
            if self.sb.target_user is not None:
                self.sb.message_users(msg)
            return out

        extra = []
        if f is not None:  # if something was provided
            # function was wrapped and an argument was handed
            if 'f' in self.__dict__:
                extra.append(f)  # first argument is not actually a function
                f = self.f  # retrieve function
                return wrapped_fn(*args, **kwargs)

            # when keyword arguments were handed to the wrapper and no arguments were handed to the function
            elif callable(f):  # True when
                return wrapped_fn
        # when the function was wrapped and no arguments were handed
        f = self.f
        return wrapped_fn(*args, **kwargs)


class RTMSlackBot(SlackBot):
    def __init__(self,
                 user_member_ids: Union[str, List[str]] = None,
                 token: str = BOT_TOKEN,
                 channel_name: str = None,
                 auto_reconnect: bool = True,
                 ping_interval: int = 10,
                 **kwargs
                 ):
        """
        A modified SlackBot class which has real time messaging (RTM) capabilities. Methods can be attached to
        RTMClient events using the RTMSlackBot.run_on decorator (this is a passthrough to the RTMClient.run_on
        decorator). The instance must be instantiated and then started separately.

        :param str, user_member_ids: Slack user ID(s) for the slack bot to be able to message user. find this by going to
            a user's profile, click the three dots (...) and there is the member ID. Example of a slack member ID: ABCDEF.
        :param str token: token to connect to slack client
        :param str channel_name: channel to message on. for example, #channelname
        :param auto_reconnect: enable/disable RTM auto-reconnect
        :param ping_interval: ping interval for RTM client
        """
        self._temp_client: slack.WebClient = None
        self.rtm_client: slack.RTMClient = slack.RTMClient(
            token=token,
            auto_reconnect=auto_reconnect,
            ping_interval=ping_interval,
        )
        slack.RTMClient.on(
            event='message',
            callback=self.run_on_message,
        )
        slack.RTMClient.on(
            event='error',
            callback=self.run_on_error,
        )
        SlackBot.__init__(
            self,
            user_member_ids=user_member_ids,
            token=token,
            channel_name=channel_name,
            **kwargs,
        )

    @property
    def _slack_client(self) -> slack.WebClient:
        """conditional slack client depending whether an RTM client is active"""
        if self.temporary_web_client is not None:
            return self.temporary_web_client
        elif self.rtm_client._web_client is not None:
            return self.rtm_client._web_client
        return self._bot_web_client

    @property
    def temporary_web_client(self) -> slack.WebClient:
        """temporary web client (e.g. if a web client was provided by an RTM event)"""
        return self._temp_client

    @temporary_web_client.setter
    def temporary_web_client(self, value: slack.WebClient):
        self._temp_client = value

    @temporary_web_client.deleter
    def temporary_web_client(self):
        self._temp_client = None

    def run_on(self, *, event: str):
        """a pass-through for the RTMClient.run_on decorator"""
        return self.rtm_client.run_on(event=event)

    def run_on_message(self, **payload):
        """method which will be run on a message event (override during subclassing to enable functionality)"""
        pass

    def run_on_error(self, **payload):
        """method which will be run on an error event (override during subclassing to enable functionality)"""
        pass

    def start_rtm_client(self):
        """starts the RTM monitor thread"""
        self.rtm_client.start()


class WebClientOverride(contextlib.AbstractContextManager):
    def __init__(self,
                 bot: RTMSlackBot,
                 web_client: slack.WebClient,
                 ):
        """
        Context manager for temporarily overriding the slack web client. This is useful for real-time-messaging
        event management while using RTMSlackBot.

        e.g.

            @slack_stream.run_on(event='message')
            def catch_message(**payload):
                web_client = payload['web_client']
                with WebClientOverride(slack_stream.bot, web_client):
                    slack_stream.bot.post_slack_message('this message will be sent immediately')


        :param bot: RTMSlackBot instance to have the web client overriden
        :param web_client: web client instance provided by a slack RTM event
        """
        self.bot = bot
        self.web_client = web_client

    def __enter__(self):
        self.bot.temporary_web_client = self.web_client

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.bot.temporary_web_client = None
