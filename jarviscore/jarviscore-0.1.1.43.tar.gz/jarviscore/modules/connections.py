from .. import Module, Log, Settings
from .. import ConfigFileNotFound
from .. import CommandMessage
from time import sleep
log = Log("CORE:Connections", verbose="log")

class Connections(Module):

    def __init__(self, channel):
        Module.__init__(self, "Connections")
        self.channel = channel
    
    def on_command(self, data: CommandMessage):
        if data.KEYWORD == "join":
            if data.args[1] != self.channel.name and (data.args[1] == data.display_name.lower() or data.user_id == "82504138"):
                self.channel.bridge.add_channel(data.args[1])
                self.channel.socket.send_message(data.channel, f"Attempting to connect to `{data.args[1]}`")
                found = False
                for channel in self.channel.bridge.channels:
                    if channel.channel_name == data.args[1]:
                        found = True
                if found:
                    self.channel.socket.send_message(data.channel, f"Connected to `{data.args[1]}`")
                    self.channel.socket.send_message(data.args[1], f"Hi there! I was invited here by '{data.display_name}' in the channel '{data.channel}'")
                    sleep(2)
                    self.channel.socket.send_message(data.args[1], f"If at any point you want me to leave your chat, use '!leave' and i'll leave you channel.")
                else:
                    self.channel.socket.send_message(data.channel, f"Was not able to connect to `{data.args[1]}`")
            else:
                log.log(f"unauthorised attempt to connect to `{data.args[1]}`")
        
        if data.KEYWORD == "leave":
            if self.channel.name == data.display_name.lower() or data.user_id == "82504138" and len(data.args) > 1:
                if data.user_id == "82504138":
                    self.channel.socket.send_message(data.channel, f"No worries! I'm outta there FutureMan")
                    self.channel.socket.send_message(data.args[1], f"Cya pal! FutureMan")
                    self.channel.bridge.remove_channel(data.args[1])
                else:
                    self.channel.socket.send_message(data.channel, f"Cya! FutureMan")
                    self.channel.bridge.remove_channel(self.channel.name)

            else:
                log.log(f"unauthorised attempt to disconnect to `{data.args[1]}`")


def setup(channel):
    try:
        settings = Settings()
        try:
            if settings.get_setting("commands.uptime") == True:
                channel.load_module(Connections(channel))
                log.log(f"[{channel.channel_name}]: Loaded Module Connections")
        except KeyError:
            channel.load_module(Connections(channel))
            log.log(f"[{channel.channel_name}]: Loaded Module Connections")
    except ConfigFileNotFound:
        channel.load_module(Connections(channel))
        log.log(f"[{channel.channel_name}]: Loaded Module Connections")

def teardown(channel):
    log.log(f"[{channel.name}]: Removed Module Connections")