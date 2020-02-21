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
import asyncio
import sched
import select
import typing
import traceback

import twitchirc  # Import self.

from .connection import RECONNECT
from .utils import _await_sync


class Bot(twitchirc.Connection):
    def schedule_event(self, delay, priority, function, args: tuple, kwargs: dict):
        """
        Schedule an event using the scheduler. Wrapper for :py:meth:`shed.scheduler.enter`

        :param delay: Delay the task will be executed in.
        :param priority: Task's priority.
        :param function: Function that will be run.
        :param args: Arguments to that function.
        :param kwargs: Keyword arguments to that function.

        :return: Event object.
        """
        return self.scheduler.enter(delay, priority, function, args, kwargs)

    def schedule_event_absolute(self, time, priority, function, args: tuple, kwargs: dict):
        """
        Schedule an event using the scheduler with a time, not a delay. Wrapper for :py:meth:`shed.scheduler.enterabs`

        :param time: Time the task will be executed.
        :param priority: Task's priority.
        :param function: Function that will be run.
        :param args: Arguments to that function.
        :param kwargs: Keyword arguments to that function.

        :return: Event object.
        """
        return self.scheduler.enterabs(time, priority, function, args, kwargs)

    def schedule_repeated_event(self, delay, priority, function, args: tuple, kwargs: dict):
        """
        Schedule a repeated event using the scheduler.

        :param delay: Delay the task will be executed in.
        :param priority: Task's priority.
        :param function: Function that will be run.
        :param args: Arguments to that function.
        :param kwargs: Keyword arguments to that function.

        :return: Event object.

        NOTE: There is currently no way to cancel an event. You have to do it manually.
        """

        def run_event():
            function()
            self.scheduler.enter(delay, priority, run_event, args, kwargs)

        return self.scheduler.enter(delay, priority, run_event, args, kwargs)

    def run_commands_from_file(self, file_object):
        lines = file_object.readlines()
        user = 'rcfile'
        channel = 'rcfile'
        self._in_rc_mode = True
        for num, i in enumerate(lines):
            i: str = i.replace('\n', '')
            if i.startswith('@'):
                if i.startswith('@at'):
                    channel = i.replace('@at ', '')
                elif i.startswith('@as'):
                    user = i.replace('@as ', '')
                continue
            m = twitchirc.ChannelMessage(user=user, channel=channel, text=i)
            m.flags = {
                'badge-info': '',
                'badges': 'moderator/1',
                'display-name': 'RCFile',
                'id': '00000000-0000-0000-0000-{:0>12}'.format(num),
                'user-id': 'rcfile',
                'emotes': ''
            }
            self._call_command_handlers(m)
        self._in_rc_mode = False

    def __init__(self, address, username: str, password: typing.Union[str, None] = None, port: int = 6667,
                 no_connect=False, storage=None, no_atexit=False, secure=False, message_cooldown=3):
        """
        A bot class.

        :param address: Address to connect to
        :param username: Username to use
        :param password: Password if needed, otherwise None can be used.
        :param port: Irc port.
        :param no_connect: Don't connect to the chat straight away.
        :param no_atexit: Don't use atexit to automatically disconnect.
        :param storage: A :py:class:`twitchirc.Storage`.
        :param secure: Use a secure connection, SSL.
        :param message_cooldown: Per-channel cooldown for messages.
        """
        super().__init__(address, port, no_atexit=no_atexit, message_cooldown=message_cooldown, secure=secure)
        self.scheduler = sched.scheduler()
        self._in_rc_mode = False
        if not no_connect:
            self.connect(username, password)
        self.username = username
        self._password = password
        self.commands: typing.List[twitchirc.Command] = []
        self.handlers: typing.Dict[str, typing.List[typing.Callable]] = {
            'pre_disconnect': [],
            'post_disconnect': [],
            'pre_save': [],
            'post_save': [],
            'start': [],
            'recv_join_msg': [],
            'recv_part_msg': [],
            'recv_ping_msg': [],
            'permission_error': [],
            'any_msg': [],
            'chat_msg': []
        }
        """
        A dict of handlers

        Available handlers:

        +----------------+----------------------------------------+---------------------------------------------------+
        |name            |arguments                               |explanation                                        |
        +================+========================================+===================================================+
        |pre_disconnect  |()                                      |                                                   |
        +----------------+----------------------------------------+---------------------------------------------------+
        |post_disconnect |()                                      |                                                   |
        +----------------+----------------------------------------+---------------------------------------------------+
        |pre_save        |()                                      |                                                   |
        +----------------+----------------------------------------+---------------------------------------------------+
        |post_save       |()                                      |                                                   |
        +----------------+----------------------------------------+---------------------------------------------------+
        |start           |()                                      |                                                   |
        +----------------+----------------------------------------+---------------------------------------------------+
        |permission_error|(message, command, missing_permissions) | message -- the ChannelMessage during which this   |
        |                |                                        | permission_error was triggered.                   |
        |                |                                        |                                                   |
        |                |                                        | command -- the Command object that triggered it.  |
        |                |                                        |                                                   |
        |                |                                        | WARN: `command` can be None if `check_permissions`|
        |                |                                        | was called (not `check_permissions_from_command`).|
        |                |                                        |                                                   |
        |                |                                        | missing_permissions -- permissions that are       |
        |                |                                        | missing to run the command.                       |
        +----------------+----------------------------------------+---------------------------------------------------+
        |any_msg         |(message)                               |                                                   |
        +----------------+----------------------------------------+---------------------------------------------------+
        |chat_msg        |(message)                               |                                                   |
        +----------------+----------------------------------------+---------------------------------------------------+        
        """

        self.prefix = '!'
        """Bot prefix. Can be set to any string. Recommended to set before registering any commands"""
        self.storage = storage
        self.on_unknown_command = 'ignore'
        """
        Action to take when an unknown command is encountered.
        Warning: This doesn't apply to commands with a forced prefix.

        Available handlers:

        * ignore - ignore it (default)
        * warn - print a warning to stdout
        * chat_message - send a chat message saying that the command is invalid.
        """
        self.permissions = twitchirc.PermissionList()
        self.command_error_handler = None
        """
        A function to handle errors being raised.
        
        Called when a command fails.
        """
        self._tasks = []

    def add_command(self, command: str,
                    forced_prefix: typing.Optional[str] = None,
                    enable_local_bypass: bool = True,
                    required_permissions: typing.Optional[typing.List[str]] = None,
                    limit_to_channels: typing.Optional[typing.List[str]]=None,
                    available_in_whispers: bool = True) \
            -> typing.Callable[[typing.Callable[[twitchirc.ChannelMessage],
                                                typing.Any]], twitchirc.Command]:
        # I'm sorry if you are reading this definition
        # here's a better version
        #  -> ((twitchirc.ChannelMessage) -> Any) -> Command
        """
        Add a command to the bot.
        This function is a decorator.

        :param command: Command to be registered.
        :param forced_prefix: Force a prefix to on this command. This is useful when you can change the prefix in \
        the bot.
        :param enable_local_bypass: If False this function will ignore the permissions \
        `twitchirc.bypass.permission.local.*`. This is useful when creating a command that can change global settings.
        :param required_permissions: Permissions required to run this command.
        :param limit_to_channels: (optional) Limit executions of the command to channels.
        :param available_in_whispers: (default True) Should the command be available in whispers?

        This is a decorator.
        """

        if required_permissions is None:
            required_permissions = []

        def decorator(func: typing.Callable) -> twitchirc.Command:
            cmd = twitchirc.Command(chat_command=command,
                                    function=func, forced_prefix=forced_prefix, parent=self,
                                    enable_local_bypass=enable_local_bypass,
                                    limit_to_channels=limit_to_channels,
                                    available_in_whispers=available_in_whispers)
            cmd.permissions_required.extend(required_permissions)
            self.commands.append(cmd)
            self.call_middleware('add_command', (cmd,), cancelable=False)
            return cmd

        return decorator

    def check_permissions(self, message: twitchirc.ChannelMessage, permissions: typing.List[str],
                          enable_local_bypass=True):
        """
        Check if the user has the required permissions to run a command

        :param message: Message received.
        :param permissions: Permissions required.
        :param enable_local_bypass: If False this function will ignore the permissions \
        `twitchirc.bypass.permission.local.*`. This is useful when creating a command that can change global settings.
        :return: A list of missing permissions.

        NOTE `permission_error` handlers are called if this function would return a non-empty list.
        """
        o = self.call_middleware('permission_check', dict(user=message.user, permissions=permissions,
                                                          message=message), cancelable=True)
        if o is False:
            return ['impossible.event_canceled']

        if isinstance(o, tuple):
            return o[1]

        missing_permissions = []
        if message.user not in self.permissions:
            missing_permissions = permissions
        else:
            perms = self.permissions.get_permission_state(message)
            if twitchirc.GLOBAL_BYPASS_PERMISSION in perms or \
                    (enable_local_bypass
                     and twitchirc.LOCAL_BYPASS_PERMISSION_TEMPLATE.format(message.channel) in perms):
                return []
            for p in permissions:
                if p not in perms:
                    missing_permissions.append(p)
        if missing_permissions:
            self.call_handlers('permission_error', message, None, missing_permissions)
        return missing_permissions

    def check_permissions_from_command(self, message: twitchirc.ChannelMessage,
                                       command: twitchirc.Command):
        """
        Check if the user has the required permissions to run a command

        :param message: Message received.
        :param command: Command used.
        :return: A list of missing permissions.

        NOTE `permission_error` handlers are called if this function would return a non-empty list.
        """
        o = self.call_middleware('permission_check', dict(user=message.user, permissions=command.permissions_required,
                                                          message=message, command=command), cancelable=True)
        if o is False:
            return ['impossible.event_canceled']

        if isinstance(o, tuple):
            return o[1]

        missing_permissions = []
        if message.user not in self.permissions:
            missing_permissions = command.permissions_required
        else:
            perms = self.permissions.get_permission_state(message)
            if twitchirc.GLOBAL_BYPASS_PERMISSION in perms or \
                    (
                            command.enable_local_bypass
                            and (twitchirc.LOCAL_BYPASS_PERMISSION_TEMPLATE.format(message.channel) in perms)
                    ):
                return []
            for p in command.permissions_required:
                if p not in perms:
                    missing_permissions.append(p)
        if missing_permissions:
            self.call_handlers('permission_error', message, command, missing_permissions)
        return missing_permissions

    def _send_if_possible(self, message, source_message):
        if isinstance(message, str):
            self.send(source_message.reply(message))
        elif isinstance(message, twitchirc.ChannelMessage):
            self.send(message)
        elif isinstance(message, list):
            for item in message:
                self._send_if_possible(item, source_message)

    def _call_command_handlers(self, message: twitchirc.ChannelMessage):
        return _await_sync(self._acall_command_handlers(message))

    async def _call_command(self, handler, message):
        o = self.call_middleware('command', {'message': message, 'command': handler}, cancelable=True)
        if o is False:
            return
        t = asyncio.create_task(handler.acall(message))
        self._tasks.append({
            'task': t,
            'source_msg': message,
            'command': handler
        })
        await self._a_wait_for_tasks()

    async def _a_wait_for_tasks(self):
        if not self._tasks:
            return
        done, _ = await asyncio.wait({i['task'] for i in self._tasks}, timeout=0.1)
        # don't pause the bot for long unnecessarily.
        for task in done:
            t = None
            for elem in self._tasks:
                if elem['task'] == task:
                    t = elem
                    break
            if t is not None:
                try:
                    result = await t['task']
                except BaseException as e:

                    for line in traceback.format_exc(1000).split('\n'):
                        twitchirc.log('warn', line)

                    if self.command_error_handler is not None:
                        self.command_error_handler(e, t['command'], t['source_msg'])
                    self._tasks.remove(t)
                    continue
                self._send_if_possible(result, t['source_msg'])
                self._tasks.remove(t)

    async def _acall_command_handlers(self, message: typing.Union[twitchirc.ChannelMessage, twitchirc.WhisperMessage]):
        """Handle commands."""
        if message.text.startswith(self.prefix):
            was_handled = False
            if ' ' not in message.text:
                message.text += ' '
            for handler in self.commands:
                if callable(handler.matcher_function) and handler.matcher_function(message, handler):
                    await self._call_command(handler, message)
                    was_handled = True
                if message.text.startswith(self.prefix + handler.ef_command):
                    await self._call_command(handler, message)
                    was_handled = True
            if not was_handled:
                self._do_unknown_command(message)
        else:
            await self._acall_forced_prefix_commands(message)

    def _call_forced_prefix_commands(self, message):
        return _await_sync(self._acall_forced_prefix_commands(message))

    async def _acall_forced_prefix_commands(self, message):
        """Handle commands with forced prefixes."""
        for handler in self.commands:
            if handler.forced_prefix is None:
                continue
            elif message.text.startswith(handler.ef_command):
                await self._call_command(handler, message)

    def _do_unknown_command(self, message):
        """Handle unknown commands."""
        if self.on_unknown_command == 'warn':
            twitchirc.warn(f'Unknown command {message!r}')
        elif self.on_unknown_command == 'chat_message':
            msg = message.reply(f'Unknown command {message.text.split(" ", 1)[0]!r}')
            self.send(msg, msg.channel)
        elif self.on_unknown_command == 'ignore':
            # Just ignore it.
            pass
        else:
            raise Exception('Invalid handler in `on_unknown_command`. Valid options: warn, chat_message, '
                            'ignore.')

    async def arun(self):
        """
        This is a coroutine version of :py:meth:`run`.

        Connect to the server if not already connected. Process messages received.
        This function includes an interrupt handler that automatically calls :py:meth:`stop`.

        :return: nothing.
        """
        try:
            await self._arun()
        except KeyboardInterrupt:
            print('Got SIGINT, exiting.')
            self.stop()
            return

    def run(self):
        """
        Connect to the server if not already connected. Process messages received.
        This function includes an interrupt handler that automatically calls :py:meth:`stop`.

        :return: nothing.
        """
        try:
            self._run()
        except KeyboardInterrupt:
            print('Got SIGINT, exiting.')
            self.stop()
            return

    def _select_socket(self):
        """Check if the socket has any data to receive."""
        sel_output = select.select([self.socket], [], [], 0.1)
        return bool(sel_output[0])

    async def _run_once(self):
        """
        Do everything needed to run, but don't loop. This can be used as a non-blocking version of :py:meth:`run`.

        :return: False if the bot should quit, True if everything went right, RECONNECT if the bot needs to reconnect.
        """
        if self.socket is None:  # self.disconnect() was called.
            return False
        if not self._select_socket():  # no data in socket, assume all messages where handled last time and return
            return True
        twitchirc.log('debug', 'Receiving.')
        o = self.receive()
        if o == RECONNECT:
            return RECONNECT
        twitchirc.log('debug', 'Processing.')
        self.process_messages(100, mode=2)  # process all the messages.
        twitchirc.log('debug', 'Calling handlers.')
        for i in self.receive_queue.copy():
            twitchirc.log('debug', '<', repr(i))
            self.call_handlers('any_msg', i)
            if isinstance(i, twitchirc.PingMessage):
                self.force_send('PONG {}\r\n'.format(i.host))
                if i in self.receive_queue:
                    self.receive_queue.remove(i)
                continue
            elif isinstance(i, twitchirc.ReconnectMessage):
                self.receive_queue.remove(i)
                return RECONNECT
            elif isinstance(i, twitchirc.ChannelMessage):
                self.call_handlers('chat_msg', i)
                await self._acall_command_handlers(i)
            elif isinstance(i, twitchirc.WhisperMessage):
                await self._acall_command_handlers(i)
            if i in self.receive_queue:  # this check may fail if self.part() was called.
                self.receive_queue.remove(i)
        if not self.channels_connected:  # if the bot left every channel, stop processing messages.
            return False
        self.flush_queue(max_messages=100)
        return True

    async def _arun(self):
        """
        Brains behind :py:meth:`run`. Doesn't include the `KeyboardInterrupt` handler.

        :return: nothing.
        """
        if self.socket is None:
            self.connect(self.username, self._password)
        self.hold_send = False
        self.call_handlers('start')
        while 1:
            run_result = await self._run_once()
            if run_result is False:
                twitchirc.log('debug', 'break')
                break
            if run_result == RECONNECT:
                self.call_middleware('reconnect', (), False)
                self.disconnect()
                self.connect(self.username, self._password)
            self.scheduler.run(blocking=False)
            await self._a_wait_for_tasks()
            await asyncio.sleep(0)

    def _run(self):
        """
        Runs :py:meth:`_arun`.

        :return: nothing.
        """
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self._arun())

    def call_handlers(self, event, *args):
        """
        Call handlers for `event`

        :param event: The event that happened. See `handlers`
        :param args: Arguments to give to the handler.

        :return: nothing.
        """
        if event not in ['any_msg', 'chat_msg']:
            twitchirc.log('debug', f'Calling handlers for event {event!r} with args {args!r}')
        for h in self.handlers[event]:
            h(event, *args)

    def disconnect(self):
        """
        Disconnect from the server.

        :return: nothing.
        """
        self.call_handlers('pre_disconnect')
        super().disconnect()
        self.call_handlers('post_disconnect')

    def stop(self):
        """
        Stop the bot and disconnect.
        This function force saves the `storage` and disconnects using :py:meth:`disconnect`

        :return: nothing.
        """
        if self.socket is None:  # Already disconnected.
            return
        self.call_handlers('pre_save')
        self.storage.save(is_auto_save=False)
        self.call_handlers('post_save')
        self.disconnect()

    def send(self, message: typing.Union[str, twitchirc.ChannelMessage], queue='misc') -> None:
        """
        Send a message to the server.

        :param message: message to send
        :param queue: Queue for the message to be in. This will be automatically overridden if the message is a \
        ChannelMessage. It will be set to :py:meth:`ChannelMessage.channel`.

        :return: nothing

        NOTE The message will not be sent instantly and this is intended. If you would send lots of messages Twitch
        will not forward any of them to the chat clients.
        """
        if self._in_rc_mode:
            if isinstance(message, twitchirc.ChannelMessage):
                twitchirc.log('info', f'[OUT/{message.channel}, {queue}] {message.text}')
            else:
                twitchirc.log('info', f'[OUT/?, {queue}] {message}')
        else:
            super().send(message, queue)
