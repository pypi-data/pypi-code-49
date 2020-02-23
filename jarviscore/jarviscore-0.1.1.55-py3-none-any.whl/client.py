from .bridge import Bridge
from .errors import NoChannelsSet, NoNickError, NoTokenError, JarvisException
import asyncio


class Client():
    """
    Base Client for the Jarvis Twitch Bot. Bots should be derived from this class.
    """
    channels: list
    nick: str
    token: str
    bridge: Bridge


    def __init__(self, nick, token, channel = None, channels = None, use_connected_channels=False):
        self.nick = nick
        self.token = token
        self.connected = use_connected_channels
        if channel is None and channels is None: 
            raise NoChannelsSet("Set either the `channel` parameter with a string, or the `channels` parameter with a list of strings.")
        self.__setup(channel=channel, channels=channels)
        self.bridge = Bridge(self)
        

    def start(self):
        try:
            if len(self.channels) > 0:
                if self.nick is not None and self.nick != "":
                    if self.token is not None and self.token != "":
                        #print("connecting to bridge")
                        self.bridge.run(self.connected)
                    else:
                        raise NoTokenError("No Token provided, provide a token or oauth value to the token attribute.")
                else:
                    raise NoNickError("Set the nick attribute with a nickname that matches the account of your bot")
            else:
                raise NoChannelsSet("No channels are set, make sure there are channels to connect to")
        except AttributeError as e:
            raise NoChannelsSet("No channels are set, make sure there are channels to connect to")

    def __setup(self, channel, channels):
        if channel is not None:
            self.channels = [channel, self.nick]
        else:
            self.channels = channels
            self.channels.append(self.nick)
        self.__normalise_channels()



    def __normalise_channels(self):
        chennel_set = []
        for channel in self.channels:
            chennel_set.append(str(channel).lower())
        self.channels = chennel_set


    def set_interval(self, interval: int):
        self.bridge.set_interval(interval)
    
    def check_messages(self, channel_list: dict):
        pass

    def on_add_channel(self, channel: str, channel_id: int):
        pass

    def on_remove_channel(self, channel: str):
        pass

