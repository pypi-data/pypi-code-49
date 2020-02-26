#!/usr/bin/env python3

""" AD1459, an IRC Client

  Copyright ©2019-2020 by Gaven Royer

  Permission to use, copy, modify, and/or distribute this software for any
  purpose with or without fee is hereby granted, provided that the above
  copyright notice and this permission notice appear in all copies.

  THE SOFTWARE IS PROVIDED "AS IS" AND ISC DISCLAIMS ALL WARRANTIES WITH REGARD
  TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
  FITNESS. IN NO EVENT SHALL ISC BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR
  CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE,
  DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS
  ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS
  SOFTWARE.

  Handling for networks and their rooms.
"""

from asyncio import get_event_loop, run_coroutine_threadsafe
import logging
import time

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib

from .widgets.room_row import RoomRow
from .widgets.message_row import MessageRow
from .client import Client
from .commands import Commands
from .formatting import Parser
from .room import Room

class Network:
    """An IRC network to connect to and chat on.

    Attributes:
        rooms (list of :obj:`Room`): A list of the joined rooms on this network.
        name (str): The user-defined name for this network.
        auth (str): The user-authentication for this network. 'sasl', 'pass', 
            or 'none'.
        host (str): The hostname for the server to connect to.
        port (int): The port number to use.
        tls (bool): Wheter the connection uses TLS encryption.
        nickname (str): The user's nickname on this network.
        realname (str): The user's Real Name on this network.
        password (str): The authentication for the password on this network.
        app (:obj:`Ad1459Application`): The app we're running on.
    """
    cmd = Commands()
    commands = {
        '/me': cmd.me,
        '/join': cmd.join,
        '/quit': cmd.quit,
        '/part': cmd.part,
        '/kick': cmd.kick,
        '/ban': cmd.ban,
        '/kickban': cmd.kickban,
        # '/cycle': cmd.cycle,
        '/nick': cmd.nick,
        '/query': cmd.query,
        '/msg': cmd.msg,
        '/whisper': cmd.query,
        '/notice': cmd.notice,
        '/topic': cmd.topic
    }

    def __init__(self, app, window):
        self.log = logging.getLogger('ad1459.network')
        self.log.debug('Creating network')
        self.app = app
        self.parser = Parser()
        self.window = window
        self.rooms = []
        self._config = {
            'name': 'New Network',
            'auth': 'sasl',
            'host': 'chat.freenode.net',
            'port': 6697,
            'tls': True,
            'nickname': 'ad1459-user',
            'username': 'ad1459-user',
            'realname': 'AD1459 User',
            'password': 'hunter2'
        }
        self.client = None

    # Synchronous Methods for this object.
    def connect(self):
        """ Connect to the network."""
        if not self.host == 'test':
            if self.client:
                if self.client.connected:
                    self.log.info('Disconnecting from %s', self.host)
                    self.disconnect()

            elif self.auth == 'sasl':
                self.client = Client(
                    self.nickname, 
                    self, 
                    sasl_password=self.password, 
                    sasl_username=self.username
                )
            else:
                self.client = Client(self.nickname, self)
            
            self.log.debug('Spinning up async connection to %s', self.host)
            self.client.username = self.username
            self.server_room = Room(self.app, self, self.window, self.name)
            self.server_room.kind = "server"
            self.add_room(self.server_room)

            # Actually do the connection
            if self.auth == 'pass':
                self.log.debug('Using password authentication')
                run_coroutine_threadsafe(
                    self.client.connect(
                        hostname=self.host,
                        port=self.port,
                        tls=self.tls,
                        password=self.password
                    ),
                    loop=get_event_loop()
                )

            else:
                self.log.debug('Using SASL authentication (or none)')
                run_coroutine_threadsafe(
                    self.client.connect(
                        hostname=self.host,
                        port=self.port,
                        tls=self.tls
                    ),
                    loop=get_event_loop()
                )
        else:
            from .testclient import TestClient
            self.generate_test_data()
            self.client = TestClient(
                    self.nickname, 
                    self, 
                    sasl_password=self.password, 
                    sasl_username=self.username
            )

            self.server_room = Room(self.app, self, self.window, self.name)
            self.server_room.kind = "server"
            self.add_room(self.server_room)

            run_coroutine_threadsafe(
                self.client.connect(
                    hostname=self.host,
                    port=self.port,
                    tls=self.tls
                ),
                loop=get_event_loop()
            )

            for channel in self.client.channels:
                room = Room(self.app, self, self.window, channel, test=True)
                room.kind = 'channel'
                self.add_room(room)
            
            popup = self.window.header.server_popup
            popup.reset_all_text()
            popup.layout_grid.set_sensitive(True)
            self.do_connected()
    
    def disconnect(self, message='AD1459 Quit'):
        """Disconnect from this network."""
        self.log.debug('Disconnecting from %s', self.name)
        run_coroutine_threadsafe(
            self.client.quit(message='AD1459 Quit'),
            loop=get_event_loop()
        )
    
    def change_nick(self, new_nick):
        """ Changes the user's nick.
        
        Arguments:
            new_nick (str): The new nickname to use.
        """
        run_coroutine_threadsafe(
            self.client.set_nickname(new_nick),
            loop=get_event_loop()
        )

    def join_channel(self, channel):
        """ Joins a room on the network.
        
        Arguments:
            channel (str): The name of the channel to join.
        """
        run_coroutine_threadsafe(
            self.client.join(channel), loop=get_event_loop()
        )

    def add_room(self, room):
        """Adds a room to this network and adds it to the UI.
        
        Arguments:
            room (:obj:`Room`): The room object to add
        """
        self.log.debug('Adding room %s to the window', room.name)
        self.window.switcher.add_row(room.row)
        self.window.message_stack.add_named(room.buffer, room.id)
        self.window.topic_stack.add_named(room.topic_pane, room.id)
        self.window.show_all()
        self.window.switcher.invalidate_sort()
        self.rooms.append(room)
    
    def get_room_for_name(self, name):
        """ Gets a room object given the name.
        
        Arguments:
            name (str): The name of the room to join
        """
        for room in self.rooms:
            if room.name == name:
                return room

        if not name.startswith('#'):
            new_room = Room(self.app, self, self.window, name)
            new_room.kind = 'dialog'
            new_room.name = name
            new_room.topic_pane.update_topic()
            self.add_room(new_room)
            self.window.switcher.invalidate_sort()
            return new_room
    
    def send_message(self, room, message):
        """ Sends a message/PRIVMSG to a channel/user.
        
        Arguments:
            room (:obj:`Room`): The room to send the message to. This is a 
                PM room or a channel.
            message (str): The message to send
        """
        message_text = self.parser.format_text(message)
        for command in self.commands:
            if not message.startswith(command):
                continue
            else:
                message_text = message_text.replace(command, '')
                self.log.debug('Got command: %s (%s)', command, message_text)
                self.commands[command](room, self, message_text)
                return 0

        self.log.debug('Sending message to %s: %s', room.name, message_text)
        run_coroutine_threadsafe(
            self.client.message(room.name, message_text),
            loop=get_event_loop()
        )
    
    # Asynchronous Callbacks
    async def on_connected(self):
        self.log.debug('Firing network.on_connected')
        """ Called upon connection to IRC."""
        self.log.info('Connected to %s', self.name)
        GLib.idle_add(self.do_connected)
    
    def do_connected(self):
        self.log.debug('Sync: running network.do_connected')
        popup = self.window.header.server_popup
        popup.reset_all_text()
        popup.layout_grid.set_sensitive(True)
        self.window.header.spinner.stop()
        self.window.switcher.invalidate_sort()
    
    async def on_nick_change(self, old, new):
        self.log.debug('Firing network.on_nick_change')
        self.log.debug('Nick %s changed to %s', old, new)
        GLib.idle_add(self.do_nick_change, old, new)
    
    def do_nick_change(self, old, new):
        self.log.debug('Sync: running network.do_nick_change')
        if old == self.nickname or old == '<unregistered>':
            self.nickname = new
            self.window.nick_button.set_label(self.nickname)
        
        else:
            for room in self.rooms:
                if new in room.users:
                    room.add_message(f'{old} is now {new}.', kind='server')
                    room.window.show_all()
                    room.update_users()
    
    async def on_join(self, channel, user):
        self.log.debug('Firing network.on_join')
        self.log.debug('%s has joined %s', user, channel)
        GLib.idle_add(self.do_join, channel, user)
    
    def do_join(self, channel, user):
        self.log.debug('Sync: running network.do_join')
        if user == self.nickname:
            new_channel = Room(self.app, self, self.window, channel)
            new_channel.kind = 'channel'
            new_channel.name = channel
            new_channel.topic_pane.update_topic()
            self.add_room(new_channel)
            new_channel.update_users()
            self.window.switcher.invalidate_sort()
            self.window.switcher.switcher.select_row(new_channel.row)
        
        else:
            room = self.get_room_for_name(channel)
            room.add_message(f'{user} joined.', kind='server')
            self.window.show_all()
            room.update_users()
    
    async def on_part(self, channel, user, message=None):
        self.log.debug('Firing network.on_part')
        self.log.debug('%s has left %s, (%s)', user, channel, message)
        GLib.idle_add(self.do_part, channel, user, message)
    
    def do_part(self, channel, user, message=None):
        self.log.debug('Sync: running network.do_part')
        room = self.get_room_for_name(channel)
        if user == self.nickname:
            room.leave()
            room.network.server_room.add_message(
                f'You have left {room.name}', kind='server'
            )
            self.rooms.remove(room)
            self.window.switcher.invalidate_sort()
        
        else:
            room.update_users()
            room.add_message(f'{user} left ({message}).', kind='server')
            self.window.show_all()
    
    async def on_kick(self, channel, target, by, reason=None):
        self.log.debug('Firing network.on_kick')
        GLib.idle_add(self.do_kick, channel, target, by, reason)
    
    def do_kick(self, channel, target, by, reason=None):
        self.log.debug('Sync: running network.do_kick')
        room = self.get_room_for_name(channel)
        if target == self.nickname:
            room.leave()
            room.network.server_room.add_message(
                f'You were kicked from {room.name} by {by}, reason: "{reason}"', 
                kind='server'
            )
            room.network.server_room.row.set_icon('emblem-important-symbolic')
            self.rooms.remove(room)
            self.window.switcher.invalidate_sort()
        
        else:
            room.update_users()
            room.add_message(
                f'{target} kicked by {by},({reason}).', kind='server'
            )
            self.window.show_all()

    async def on_quit(self, user, message=None):
        self.log.debug('Firing network.on_quit')
        self.log.debug('%s has quit! (%s)', user, message)
        GLib.idle_add(self.do_quit, user, message)
    
    def do_quit(self, user, message=None):
        self.log.debug('Sync: running network.do_quit')
        qmessage = f'{user} quit ({message}).'
        for room in self.rooms:
            if user in room.old_users:
                room.add_message(qmessage, kind='server')
                room.update_users()
    
    async def on_kill(self, target, by, reason=None):
        self.log.debug('Firing network.on_kill')
        GLib.idle_add(self.do_kill, target, by, reason)
    
    def do_kill(self, target, by, reason=None):
        self.log.debug('Sync: running network.do_kill')
        qmessage = f'{target} killed by {by}, ({reason}).'
        for room in self.rooms:
            if target in room.old_users:
                room.add_message(qmessage, kind='server')
                room.update_users()
    
    async def on_message(self, target, source, message):
        self.log.debug('Firing network.on_message')
        GLib.idle_add(self.do_message, target, source, message)
    
    def do_message(self, target, source, message):
        self.log.debug('Sync: running network.do_message')
        if target.startswith('#'):
            room = self.get_room_for_name(target)
            self.log.debug('Adding message to %s', room.id)
            room.add_message(message, source)
            room.update_tab_complete(source)
            self.window.show_all()

    async def on_notice(self, target, source, message):
        self.log.debug('Firing network.on_notice')
        self.log.debug('%s noticed to %s: %s', source, target, message)
        GLib.idle_add(self.do_notice, target, source, message)
    
    def do_notice(self, target, source, message):
        self.log.debug('Sync: running network.do_notice')
        if target.startswith('#'):
            room = self.get_room_for_name(target)
            self.log.debug('Adding notice to %s', room.id)
            room.add_message(message, source, kind='notice')
            room.update_tab_complete(source)
            self.window.show_all()
    
    async def on_private_message(self, target, source, message):
        self.log.debug('Firing network.on_private_message')
        self.log.debug('PM to %s from %s: %s', target, source, message)
        GLib.idle_add(self.do_private_message, target, source, message)

    def do_private_message(self, target, source, message):
        self.log.debug('Sync: running network.do_private_message')
        if target == self.nickname:
            room = self.get_room_for_name(source)
            self.log.debug('Adding message from %s', room.id)
        else:
            room = self.get_room_for_name(target)
            self.log.debug('Adding message to %s', room.id)
        
        room.add_message(message, source)
        self.window.show_all()
    
    async def on_private_notice(self, target, source, message):
        self.log.debug('Firing network.on_private_notice')
        self.log.debug('Private Notice to %s from %s: %s', target, source, message)
        GLib.idle_add(self.do_private_notice, target, source, message)
        
    def do_private_notice(self, target, source, message):
        self.log.debug('Sync: running network.do_private_notice')
        if target == self.nickname:
            room = self.get_room_for_name(source)
            self.log.debug('Adding message from %s', room.id)
        else:
            room = self.get_room_for_name(target)
            self.log.debug('Adding message to %s', room.id)

        self.log.debug('Adding notice from %s', room.id)
        room.add_message(message, source, kind='notice')
        self.window.show_all()
    
    async def on_topic_change(self, channel, message, by):
        self.log.debug('Firing network.on_topic_change')
        GLib.idle_add(self.do_topic_change, channel, message, by)
    
    def do_topic_change(self, channel, message, by):
        self.log.debug('Sync: running network.do_topic_change')
        self.log.debug('Changing topic in %s', channel)
        room = self.get_room_for_name(channel)
        room.topic_pane.update_topic()
        room.add_message(
            f'{by} set the topic to "{message}"', kind='server'
        )
    
    async def on_mode_change(self, channel, modes, by):
        self.log.debug('Firing network.on_mode_change')
        GLib.idle_add(self.do_mode_change, channel, modes, by)

    def do_mode_change(self, channel, modes, by):
        self.log.debug('Sync: running network.do_mode_change')
        room = self.get_room_for_name(channel)
        mode_codes = modes[0]
        mode_index = 1
        change = None
        last_code = ''
        mode_msg = f'{by} '
        try:
            for code in mode_codes:
                if code == last_code:
                    mode_msg += f'{modes[mode_index]}, '
                    mode_index += 1
                
                elif code == '+':
                    change = 'set'
                
                elif code == '-':
                    change = 'removed'
                
                elif code == 'b':
                    if change == 'set':
                        mode_msg += f'banned {modes[mode_index]}, '
                        mode_index += 1
                    else:
                        mode_msg += f'unbanned {modes[mode_index]}, '
                        mode_index += 1

                
                elif code == 'c':
                    if change == 'set':
                        mode_msg += 'disabled colours, '
                    else:
                        mode_msg += 'enabled colours, '
                
                elif code == 'e':
                    mode_msg += f'{change} a ban exemption on {modes[mode_index]}, '
                    mode_index += 1
                
                elif code == 'C':
                    if change == 'set':
                        mode_msg += 'disabled CTCP, '
                    else:
                        mode_msg += 'enabled CTCP, '
                
                elif code == 'i':
                    if change == 'set':
                        mode_msg += f'made {channel} invite-only, '
                    else:
                        mode_msg += f'made {channel} open, '

                elif code == 'o':
                    if change == 'set':
                        mode_msg += f'opped {modes[mode_index]}, '
                        mode_index += 1
                    else:
                        mode_msg += f'deopped {modes[mode_index]}, '
                        mode_index += 1
                
                elif code == 'v':
                    if change == 'set':
                        mode_msg += f'voiced {modes[mode_index]}, '
                        mode_index += 1
                    else:
                        mode_msg += f'devoiced {modes[mode_index]}, '
                        mode_index += 1
                
                elif code == 'q':
                    if change == 'set':
                        mode_msg += f'muted {modes[mode_index]}, '
                        mode_index += 1
                    else:
                        mode_msg += f'unmuted {modes[mode_index]}, '
                        mode_index += 1
                
                elif code == 'm':
                    mode_msg += f'{change} moderated, '

                last_code = code
        
        except IndexError:
            print('No index %s', mode_index)
        
        mode_msg = mode_msg.strip()
        mode_msg = mode_msg.strip(',')
        room.add_message(f'{mode_msg}.', kind='server')
        room.update_users()

    async def on_user_invite(self, target, channel, by):
        self.log.debug('Firing network.on_user_invite')
        GLib.idle_add(self.do_user_invite, target, channel, by)
    
    def do_user_invite(self, target, channel, by):
        self.log.debug('Sync: running network.do_user_invite')
        room = self.get_room_for_name(channel)
        room.add_message(f'{by} invited {target}', kind='server')

    async def on_invite(self, channel, by):
        self.log.debug('Firing network.on_invite')
        GLib.idle_add(self.do_invite, channel, by)
    
    def do_invite(self, channel, by):
        self.log.debug('Sync: running network.do_invite')
        self.server_room.add_message(
            f'You were invited to {channel} by {by}', kind='server'
        )
        self.server_room.row.set_icon('emblem-important-symbolic')


    async def on_ctcp_action(self, target, source, action):
        self.log.debug('Firing network.on_ctcp_action')
        self.log.debug('Action in %s from %s: %s %s', target, source, source, action )
        GLib.idle_add(self.do_ctcp_action, target, source, action)
        
    def do_ctcp_action(self, target, source, action):
        self.log.debug('Sync: running network.do_ctcp_action')
        self.log.debug('Adding action from %s to %s', source, target)
        if target.startswith('#'):
            room = self.get_room_for_name(target)
        elif target == self.nickname:
            room = self.get_room_for_name(source)
        
        message = f'\x1D{source} {action}\x1D'
        room.add_message(message, sender="**", kind='action')
        self.window.show_all()
        room.update_tab_complete(source)

    # Data for this object.
    @property
    def name(self):
        """str: The name of this network (and its room)."""
        return self._config['name']
    
    @name.setter
    def name(self, name):
        """This is actually tracked by the room."""
        self.log.debug('Setting name to %s', name)
        self._config['name'] = name
    
    @property
    def auth(self):
        """str: One of 'sasl', 'pass', or 'none'."""
        return self._config['auth']
    
    @auth.setter
    def auth(self, auth):
        """Only set if it's a valid value."""
        if auth == 'sasl' or auth == 'pass' or auth == 'none':
            self._config['auth'] = auth

    @property
    def host(self):
        """str: The hostname of the server to connect to."""
        return self._config['host']
    
    @host.setter
    def host(self, host):
        self._config['host'] = host
    
    @property
    def port(self):
        return self._config['port']
    
    @port.setter
    def port(self, port):
        """ Only set a port that is within the valid range."""
        if port > 0 and port <= 65535:
            self._config['port'] = int(port)

    @property
    def tls(self):
        """bool: Whether or not to use TLS"""
        return self._config['tls']
    
    @tls.setter
    def tls(self, tls):
        self._config['tls'] = tls

    @property
    def nickname(self):
        """str: The user's nickname"""
        return self._config['nickname']
    
    @nickname.setter
    def nickname(self, nickname):
        self.log.debug('Setting nickname to %s', nickname)
        self._config['nickname'] = nickname

    @property
    def username(self):
        """str: The username to use for the connection"""
        return self._config['username']
    
    @username.setter
    def username(self, username):
        self.log.debug('Setting username to %s', username)
        self._config['username'] = username

    @property
    def realname(self):
        """str: The user's real name"""
        return self._config['realname']
    
    @realname.setter
    def realname(self, realname):
        self._config['realname'] = realname

    @property
    def password(self):
        """str: The user's password."""
        return self._config['password']
    
    @password.setter
    def password(self, password):
        self.log.debug('Setting password')
        self._config['password'] = password

    # Junk Data, for taking screenshots
    def generate_test_data(self):
        self.name = 'IRC Server'
        self.auth = 'sasl'
        self.host = 'test'
        self.port = 6697
        self.tls = True
        self.nickname = 'Composedly'
        self.username = 'testing'
        self.realname = 'Comp O. Sedly'
        self.password = 'hunter2'