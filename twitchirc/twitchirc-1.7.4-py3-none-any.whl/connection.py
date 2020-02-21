#  Library to make crating bots for Twitch chat easier.
#  Copyright (c) 2019 Maciej Marciniak
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
import atexit
import socket
import ssl
import time
import typing

import twitchirc  # Import self.

RECONNECT = 'RECONNECT'


def to_bytes(obj, encoding='utf-8'):
    if isinstance(obj, str):
        return bytes(obj, encoding)
    else:
        return bytes(obj)


class Connection:
    def call_middleware(self, action, arguments, cancelable) -> typing.Union[bool, typing.Tuple[bool, typing.Any]]:
        """
        Call all middleware.

        :param action: Action to run.
        :param arguments: Arguments to give, depends on which action you use, for more info see AbstractMiddleware.
        :param cancelable: Can the event be canceled?
        :return: False if the event was canceled, True otherwise.
        """
        event = twitchirc.Event(action, arguments, source=self, cancelable=cancelable)
        canceler: typing.Optional[twitchirc.AbstractMiddleware] = None
        for m in self.middleware:
            m.on_action(event)
            if not canceler and event.canceled:
                canceler = m
        if event.canceled:
            twitchirc.log('debug', f'Event {action!r} was canceled by {canceler.__class__.__name__}.')
            return False
        if event.result is not None:
            return True, event.result
        return True

    def __init__(self, address: str, port: int = 6667, message_cooldown: int = 3, no_atexit=False,
                 secure: bool = False):
        """
        A bare-bones connection class.

        :param address: Address to connect to.
        :param port: Irc port.
        :param no_atexit: Don't use atexit to automatically disconnect.
        :param secure: Use a secure connection, SSL.
        :param message_cooldown: Per-channel cooldown for messages.
        """
        self.middleware: typing.List[twitchirc.AbstractMiddleware] = []
        """
        Enabled middleware. Each entry in this list should be an instance of a subclass of \
        :py:class:`twitchirc.AbstractMiddleware`
        """

        self.message_cooldown: int = message_cooldown
        """Per-channel cooldown for messages."""
        self.address: str = address
        """Address to connect to."""
        self.port: int = port
        self.socket: typing.Union[socket.socket, None] = None
        self.queue: typing.Dict[str, typing.List[bytes]] = {
            'misc': []
        }
        self.receive_queue: typing.List[
            typing.Union[twitchirc.Message, twitchirc.ChannelMessage, twitchirc.PingMessage]] = []
        self.receive_buffer: str = ''
        self.message_wait: typing.Dict[str, float] = {
            'misc': time.time()
        }
        self.hold_send = False
        """Stop sending messages for a bit, improper use of this may hang your program."""

        self.channels_connected = []
        """All channels that the Connection is listening to."""
        self.channels_to_remove = []
        self.secure = secure
        self.last_ping = 0.0

        if not no_atexit:
            @atexit.register
            def close_self():
                try:
                    self.disconnect()
                    twitchirc.log('info', 'Automatic disconnect: ok.')
                except Exception as e:
                    twitchirc.log('info', f'Automatic disconnect: fail ({e})')

    def moderate(self, channel: str, user: typing.Optional[str] = None, message_id: typing.Optional[str] = None):
        """
        Construct a ModerationContainer targeting the channel, and optionally a user and message.

        :return: Newly created ModerationContainer
        """
        return twitchirc.ModerationContainer(message_id, user, channel, parent=self)

    def join(self, channel):
        """
        Join a channel.

        :param channel: Channel you want to join.
        :return: nothing.
        """
        twitchirc.log('debug', 'Joining channel {}'.format(channel))

        o = self.call_middleware('join', dict(channel=channel), True)
        if o is False:
            return

        self.force_send('join #{}\r\n'.format(channel))
        self.queue[channel] = []
        self.message_wait[channel] = time.time()
        self.channels_connected.append(channel)

    def part(self, channel):
        """
        Leave a channel

        :param channel: Channel you want to leave.
        :return: nothing.
        """
        o = self.call_middleware('part', dict(channel=channel), cancelable=True)
        if o is False:
            return
        twitchirc.log('debug', f'Departing from channel {channel}')
        self.force_send(f'part #{channel}\r\n')
        self.channels_to_remove.append(channel)

    def disconnect(self):
        """
        Disconnect from IRC.

        :return: nothing.
        """
        self.call_middleware('disconnect', {}, cancelable=False)

        self.socket.send(b'quit\r\n')
        self.socket.shutdown(socket.SHUT_WR)
        self.socket.close()
        self.socket = None

    def twitch_mode(self):
        self.cap_reqs()

    def cap_reqs(self, use_membership=True):
        """
        Send CAP REQs.

        :param use_membership: Send the membership capability.
        :return: nothing.
        """
        twitchirc.log('debug', f'Sending CAP REQs. Membership: {use_membership}')
        self.force_send(f'CAP REQ :twitch.tv/commands twitch.tv/tags'
                        f'{" twitch.tv/membership" if use_membership else ""}\r\n')

    def connect(self, username, password: typing.Union[str, None] = None) -> None:
        """
        Connect to the IRC server.

        :param username: Username that will be used.
        :param password: Password to be sent. If None the PASS packet will not be sent.
        """
        self.call_middleware('connect', dict(username=username), cancelable=False)
        twitchirc.info('Connecting...')
        self._connect()
        twitchirc.log('debug', 'Logging in...')
        self._login(username, password)
        twitchirc.log('debug', 'OK.')
        self.last_ping = time.time()

    def ping(self) -> None:
        """Send a PING to the server"""
        twitchirc.log('debug', 'Sent ping')
        self.force_send(twitchirc.PingMessage(str(time.time())))

    def on_receive_pong(self, pong: twitchirc.PongMessage):
        latency = self.last_ping - float(pong.host)

    def _login(self, username, password: typing.Union[str, None] = None):
        """
        Send NICK and PASS. For external use use :py:meth:`connect`.

        :return: nothing.
        """
        self.username = username
        self._password = password
        if password is not None:
            self.force_send('PASS {}\r\n'.format(password))
        else:
            self.force_send('PASS this_looks_like_a_password_ok?\r\n')
        self.force_send('NICK {}\r\n'.format(username))

    def _connect(self):
        """
        Connect to the IRC server. For external use use :py:meth:`connect`.

        :return: nothing.
        """
        if self.secure:
            sock = socket.socket()
            sock.connect((self.address, self.port))
            self._ssl_context = ssl.create_default_context()
            self.socket = self._ssl_context.wrap_socket(sock, server_hostname=self.address)
        else:
            self.socket = socket.socket()
            self.socket.connect((self.address, self.port))

    def send(self, message: typing.Union[str, twitchirc.ChannelMessage], queue='misc') -> None:
        """
        Queue a packet to be sent to the server.

        For sending a packet immediately use :py:meth:`force_send`.

        :param message: Message to be sent to the server.
        :param queue: Queue name. This will be automatically overridden if the message is a ChannelMessage. It will \
        be set to `message.channel`.
        :return: Nothing
        """
        o = self.call_middleware('send', dict(message=message, queue=queue), cancelable=True)
        if o is False:
            twitchirc.log('debug', str(message), ': canceled')
            return

        if isinstance(message, twitchirc.ChannelMessage):
            if message.user == 'rcfile':
                twitchirc.info(str(message))
                return
            queue = message.channel
        if self.socket is not None or self.hold_send:
            twitchirc.log('debug', 'Queued message: {}'.format(message))
            if queue not in self.queue:
                self.queue[queue] = []
                self.message_wait[queue] = time.time()
            msg = to_bytes(message, 'utf-8')
            if len(self.queue[queue]) and self.queue[queue][-1] == msg:
                msg += bytes('\U0000e000', 'utf-8')
            self.queue[queue].append(to_bytes(message, 'utf-8'))
        else:
            twitchirc.warn(f'Cannot queue message: {message!r}: Not connected.')

    def force_send(self, message: typing.Union[str, twitchirc.Message]):
        """
        Send a message immediately, without making it wait in the queue.
        For queueing a message use :py:meth:`send`.

        :param message: Message to be sent to the server.
        :return: Nothing
        """
        # Call it VIP queue if you wish. :)
        o = self.call_middleware('send', dict(message=message, queue='__force_send__'), cancelable=True)
        if o is False:
            return
        if isinstance(o, tuple):
            message = o[1]

        twitchirc.log('debug', 'Force send message: {!r}'.format(message))
        self.queue['misc'].insert(0, to_bytes(message, 'utf-8'))
        self.flush_single_queue('misc', no_cooldown=True)

    def _send(self, message: bytes):
        """Send some data straight to the socket. If it is none do nothing."""
        if self.socket is None:
            return
        self.socket.send(message)

    def flush_single_queue(self, queue, no_cooldown=False, max_messages=1, now=None):
        """
        Send waiting messages.

        :param queue: Queue to flush.
        :param no_cooldown: Don't wait for cooldowns.
        :param max_messages: Maximum messages to send.
        :param now: Current time.
        :return: Number of messages sent.
        """
        if now is None:
            now = time.time()
        if self.hold_send:
            return 0
        if self.message_wait[queue] > now and not no_cooldown:
            return 0
        sent = 0
        for num, message in enumerate(self.queue[queue][:max_messages]):
            twitchirc.info(f'Sending message {message!r}')
            self._send(message)
            sent += 1
            self.message_wait[queue] = now + self.message_cooldown
        self.queue[queue] = self.queue[queue][max_messages:]
        return sent

    def flush_queue(self, max_messages: int = 1) -> int:
        """
        Send waiting messages

        :param max_messages: Maximum amount messages to send.
        :return: Amount of messages sent.
        """
        if self.hold_send:
            return 0
        sent = 0
        now = time.time()
        for queue_name in self.queue:
            sent += self.flush_single_queue(queue_name, False, max_messages, now)
        return sent

    def receive(self):
        """Receive messages from the server and put them in the :py:attr:`receive_buffer`."""
        message = str(self.socket.recv(4096), 'utf-8', errors='ignore').replace('\r\n', '\n')
        if message == '':
            twitchirc.log('warn', 'Empty message')
            return RECONNECT
        self.receive_buffer += message

    def _remove_parted_channels(self):
        """
        Remove channels that have been parted when the respective queues got emptied.

        :return: nothing.
        """
        for i in self.channels_to_remove.copy():
            if not self.queue[i]:
                self.channels_to_remove.remove(i)
                del self.message_wait[i]
                del self.queue[i]

    def process_messages(self, max_messages: int = 1, mode=-1) -> typing.List[twitchirc.Message]:
        """
        Process the messages from self.receive_buffer
        Modes:
        * -1 every message. Nothing goes to self.receive_queue.
        * 0 chat messages. Other messages go to self.receive_queue.
        * 1 other messages. Chat messages go to self.receive_queue.
        * 2 do not return anything. Everything goes to self.receive_queue.

        :param max_messages: Maximum amount of messages to process.
        :param mode: What messages to return.
        :return: All messages specified by `mode`.
        """
        self._remove_parted_channels()
        messages_to_return = []
        messages_to_add_to_recv_queue = []
        for _ in range(max_messages):
            if '\n' not in self.receive_buffer:
                break
            message = self.receive_buffer.split('\n', 1)[0]
            self.receive_buffer = self.receive_buffer.replace(message + '\n', '', 1)
            # Remove `message` from the buffer.
            if message == '':
                continue
            m = twitchirc.auto_message(message, parent=self)
            o = self.call_middleware('receive', dict(message=m), True)
            if o is False:
                continue

            if isinstance(m, twitchirc.ChannelMessage):
                if mode in [-1, 0]:
                    messages_to_return.append(m)
                else:
                    messages_to_add_to_recv_queue.append(m)
            else:
                if mode in [-1, 1]:
                    messages_to_return.append(m)
                else:
                    messages_to_add_to_recv_queue.append(m)
        self.receive_queue.extend(messages_to_add_to_recv_queue)
        return messages_to_return

    def clone(self):
        """Creates a new connection with the same auth"""
        new = Connection(self.address, self.port, self.message_cooldown, secure=self.secure)
        new.connect(self.username, self._password)
        return new

    def clone_and_send_batch(self, message_batch: typing.List[typing.Union[str, twitchirc.ChannelMessage]]):
        """Creates a new connection with the same auth and queues all the provided messages."""
        new = self.clone()
        for i in message_batch:
            new.send(i)
        return new
