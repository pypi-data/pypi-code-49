import socket
from time import sleep


from .log import Log
# from .bridge import Bridge
from threading import Thread
from .message import RawMessage


from .messageparser import parse_line


class Socket():
    
    # bridge: Bridge
    socket: socket.socket
    buffer: str
    active: bool
    ready: bool
    channel_list: list
    log: Log


    # def __init__(self, bridge: Bridge = None):
    def __init__(self, channel, nick: str, token: str, verbose=False):
        self.name = f"Thread - {channel.channel_name} Socket"
        self.nick = nick
        self.token = token
        self.active = True
        self.verbose = verbose
        self.buffer = ""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.channel = channel
        self.log = Log(f"{channel.channel_name} Socket")
        self.__connect()
        
        

    def __connect(self):
        self.socket.connect(("irc.chat.twitch.tv", 6667))
        self._send_raw(f"PASS {self.token}")
        self._send_raw(f"NICK {self.nick}")
        self._send_raw("CAP REQ :twitch.tv/membership")
        self._send_raw("CAP REQ :twitch.tv/tags")
        self._send_raw("CAP REQ :twitch.tv/commands")
        self._send_raw(f"JOIN #{self.channel.channel_name} ")
        pass

    def disconnect(self):
        if self.verbose:
            print("departing channels")
        try:
            self._send_raw(f"PART #{self.channel.channel_name} ")
            self.socket.close()
        except Exception:
            pass

    def reconnect(self):
        if self.verbose:
            print("Reconnect detected!")
        self.disconnect()
        if self.verbose:
            print("Waiting to reconnect.")
        sleep(10)
        self.__connect()

    def connect_to_channel(self, channel: str):
        self._send_raw("JOIN #"+ channel.lower() +" ")
        # self.channel_list.append(channel)
        if self.verbose:
            print(f"connecting to '{channel}'")

    def disconnect_from_channel(self, channel: str):
        self._send_raw("PART #"+ channel.lower() +" ")
        # self.__clearchannel(channel)
        if self.verbose:
            print(f"departing from '{channel}'")

    def __clearchannel(self, channel: str):
        counter = 0
        for chn in self.channel_list:
            if chn.name == channel:
                self.channel_list.pop(counter)
                return
            counter += 1

    def listenToStream(self):
        self.__process_stream_data()


    def run(self):
        while self.active:
            self.__process_stream_data()
        try:
            self.socket.close()
        except Exception:
            pass

    def close(self):
        if self.verbose:
            print(f"({self.name}) Closing Socket")
        self.active = False
        self.socket.close()
        


    def _send_raw(self, message: str):
        try:
            self.socket.send((f"{message}\r\n").encode('utf-8'))
            if self.verbose:
                if message[:4] == "PASS":
                    print(f"({self.name}) < PASS ****")
                else:
                    print(f"({self.name}) < {message}")
        except OSError:
            self.log.error(f"Socket is closed and must be reopened to send the message '{message}'")


    def __process_stream_data(self):
        try:
            self.buffer = self.buffer + self.socket.recv(1024).decode()
        except ConnectionAbortedError:
            self.log.info("Socket connection has Closed")
        temp = self.buffer.split("\n")
        self.buffer = temp.pop()
        for line in temp:
            
            if ("PING :tmi.twitch.tv" in line): # Keep Alive Mechanism
                self._send_raw("PONG :tmi.twitch.tv")
            self.on_socket_data(line)

    
    def on_socket_data(self, line: str):
        self.on_data(parse_line(line))
        
    def on_data(self, data):
        if self.verbose:
            print(f" >", data.line)
        self.channel.on_raw(data)
        
        if data.inner == "Message":
            self.channel.on_message(data)
        elif data.inner == "Join":
            self.channel.on_join(data)
        elif data.inner == "Mode":
            self.channel.on_mode(data)
        elif data.inner == "Names":
            self.channel.on_names(data)
        elif data.inner == "Part":
            self.channel.on_part(data)
        elif data.inner == "ClearChat":
            self.channel.on_clearchat(data)
        elif data.inner == "ClearMessage":
            self.channel.on_clearmessage(data)
        elif data.inner == "HostTarget":
            self.channel.on_hosttarget(data)
        elif data.inner == "Notice":
            self.channel.on_notice(data)
        elif data.inner == "Reconnect":
            self.channel.on_reconnect(data)
        elif data.inner == "RoomState":
            self.channel.on_roomstate(data)
        elif data.inner == "UserState":
            self.channel.on_userstate(data)
        elif data.inner == "GlobalUserState":
            self.channel.on_globaluserstate(data)
        elif data.inner == "UserNotice":
            self.channel.on_usernotice(data)
        elif data.inner == "RitualUserNotice":
            self.channel.on_ritual_usernotice(data)
        elif data.inner == "BitBadgeUpgradeUserNotice":
            self.channel.on_bitbadgeupgrade_usernotice(data)
        elif data.inner == "RaidUserNotice":
            self.channel.on_raid_usernotice(data)
        elif data.inner == "Whisper":
            if data.channel == self.channel.channel_name:
                self.log.whisper (data.message_text, data.display_name)
                self.channel.on_whisper(data)
        elif data.inner == "SubscriberUserNotice":
            if data.display_name.lower() != self.nick.lower():
                self.channel.on_subscriber_usernotice(data)
        elif data.inner == "GiftedSubscriberUserNotice":
            if data.display_name.lower() != self.nick.lower():
                self.channel.on_giftedsubscriber_usernotice(data)
        elif data.inner == "PrivateMessage":
            if data.display_name.lower() != self.nick.lower():
                self.log.chat(data.message_text, data.channel, data.display_name)
                self.channel.on_privmessage(data)
        elif data.inner == "CommandMessage":
            if data.display_name.lower() != self.nick.lower():
                self.log.chat(f"[CMD] {data.message_text}",data.channel, data.display_name)
                self.channel.on_command(data)

    def join(self, channel: str):
        send = f"JOIN #{channel.lower()}"
        self._send_raw(send)

    def send_message(self, channel: str, message: str):
        send = f"PRIVMSG #{channel.lower()} :{message}"
        self._send_raw(send)
        self.log.sent(message, channel.lower())
    
    def send_action_message(self, channel: str, message: str):
        send = f"PRIVMSG #{channel.lower()} :/me {message}"
        self._send_raw(send)

    def send_whisper(self, user: str, message: str):
        send = f"PRIVMSG #{user.lower()} :/w {user.lower()} {message}"
        # send = f"PRIVMSG #{self.nick} :/w {user.lower()} {message}"
        self._send_raw(send)
        self.log.sent_whisper(message, user.lower())

    def timeout_user(self, user: str, channel: str, timeout=1):
        send = f"PRIVMSG #{channel} :/timeout {user} {timeout}"
        self._send_raw(send)

    def clear_message(self, channel: str, message_id: str):
        send = f"PRIVMSG #{channel} :/delete {message_id}"
        self._send_raw(send)

    def ban_user(self, user: str, channel: str):
        send = f"PRIVMSG #{channel} :/ban {user}"
        self._send_raw(send)
