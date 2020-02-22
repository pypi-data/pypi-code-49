from .channel import Channel, ConnectedChannel
from .httpclient import HTTPClient, WebResponse
from .log import Log
from time import sleep
from datetime import datetime


api_users = "https://api.twitch.tv/helix/users?"

class Bridge():
    """description of class"""
    channels: list
    active: bool
    


    def __init__(self, client):
        self.client = client
        self.active = True
        self.web = HTTPClient("Bridge")
        self.log = Log("CORE")
        self.lastCheck = datetime.now()
        self.__interval = 7
        pass


    
    def __init_channels(self, connected: bool):
        self.channels = []
        chns = []
        for chn in self.__get_channel_shortlist():
            response: WebResponse = self.web.GetFromTwitch(api_users+chn)
            if response.code == 200 or response.code == "200":
                for user_data in response.json["data"]:
                    chns.append({
                        "login": user_data["login"],
                        "id": user_data["id"]
                    })
            else:
                self.log.error(f"There was an issue communicating with Twitch. Details: {response.message}")
        for chan in chns:
            if connected:
                channel = ConnectedChannel(self, self.client.nick, self.client.token, chan["login"], chan["id"])
            else:
                channel = Channel(self, self.client.nick, self.client.token, chan["login"], chan["id"])
            self.channels.append(channel)
            

    def __get_channel_shortlist(self):
        out = ""
        counter = 0
        maxCount = 80
        for chn in self.client.channels:
            if counter < maxCount:
                out += f"login={chn}&"
            else:
                yield out[:-1]
                out = f"login={chn}&"
                counter = 0
        yield out[:-1]


    def __get_channel(self, name: str):
        for channel in self.channels:
            if channel.name == name:
                return channel
        



    def run(self, connected = False):
        self.__init_channels(connected)
        self.lastCheck = datetime.now()
        try:
            for channel in self.channels:
                sleep(2)
                channel.start()
            while self.active:
                sleep(0.0001)
                if (datetime.now() - self.lastCheck).seconds > self.__interval:
                    self.client.check_messages(self.channels)
                    self.heartbeat()
                    self.lastCheck = datetime.now()

        except KeyboardInterrupt:         
            for channel in self.channels:
                channel.close()

    def heartbeat(self):
        for channel in self.channels:
            channel.on_heartbeat()

    def send_message_to_channel(self, channel: str, message: str):
        for chn in self.channels:
            if chn.channel_name == channel:
                chn.send(message)

    def set_interval(self, interval: int):
        self.__interval = interval
    
    
    def add_channel(self, channel: str, id: int = None):
        if id is None:
            response: WebResponse = self.web.GetFromTwitch(f"{api_users}login={channel}")
            if response.code == 200 or response.code == "200":
                id = response.json["data"][0]["id"]
            else:
                self.log.error(f"Could not Add Channel. There was an issue communicating with Twitch. Details: {response.message}")
                return

        chn = Channel(self, self.client.nick, self.client.token, channel, id=id)
        self.channels.append(chn)
        chn.start()
        chn.on_new_connection(channel)
        self.client.on_add_channel(channel, id)
    
    def remove_channel(self, channel: str):
        for chn in self.channels:
            if chn.channel_name == channel:
                chn.close()
                self.channels.remove(chn)
        self.client.on_remove_channel(channel)





    


