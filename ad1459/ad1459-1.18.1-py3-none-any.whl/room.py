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

  Handling for rooms.
"""

import asyncio
import enum
import logging
import time as Time

import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify

from .widgets.message_buffer import MessageBuffer
from .widgets.message_row import MessageRow
from .widgets.room_row import RoomRow, RoomKind, RoomIcon
from .widgets.topic import TopicPane

class Room:
    """ A Room object that represents a list of grouped messages on IRC. This 
    can be a channel, PM conversation/dialog/query, or a list of 
    server messages.
    
    Attributes:
        buffer (:obj:): The message buffer for this room.
        topic (:obj:): The room topic (if applicable).
        row (:obj:`RoomRow`) The row for this room in the switcher.
    """

    def __init__(self, app, network, window, name, test=False):
        Notify.init('AD1459')
        self.log = logging.getLogger('ad1459.room')
        self.log.debug('Creating new room %s', name)

        self.app = app
        self.network = network 
        self.window = window

        self.name = name
        self._kind = RoomKind.CHANNEL

        self.notification = Notify.Notification.new('AD1459', 'Init')
        self.buffer = MessageBuffer(self)
        self.row = RoomRow(self)
        self.topic_pane = TopicPane(self)
        self.old_users = []
        self._tab_complete = []
        self.unsent_text = ''
        self.recents = []
    
    # Methods
    def add_message(self, message, sender='*', kind='message', time=None):
        """ Adds a message into this room and inserts it into the buffer.

        Arguments:
            message (str): the text of the message to add.
            sender (str): The person/entity who sent the message
            time (str): The time the message was sent.
            kind (str): The type of message this is (default: 'message')
        """
        if not time:
            time = Time.ctime().split()[3]
        
        if (self.network.nickname in message and kind != 'server'):
            kind = 'highlight'
        
        if sender == self.network.nickname and kind != 'server':
            kind = 'mine'

        # Create the new message
        new_message = MessageRow()
        new_message.time = time
        new_message.sender = sender
        new_message.text = message
        new_message.kind = kind

        # Get the same of the unread Icon
        current_room = self.window.message_stack.get_visible_child().room
        
        # This sets the unread indicator for the channel
        if self.window.active_room != self or not self.window.focused:
            if self.row.icon.value <= RoomIcon[kind.upper()].value:
                self.row.icon = kind
        
        # TODO: This can be improved
        # This shows the notification
        if not self.window.focused:
            if (
                    new_message.kind == 'highlight' or 
                    (self.kind == RoomKind.DIALOG and
                    new_message.kind != 'mine')
            ):
                if self.kind == RoomKind.CHANNEL:
                    self.notification.update(
                        f'{sender} mentioned you in {self.name}',
                        message
                    )
                
                else:
                    self.notification.update(
                        f'New message from {sender}',
                        message
                    )
                self.notification.show()
        
        # This posts the message, in either the last server message or a new one
        messages = self.buffer.list_box.get_children()
        if messages:
            last_message = messages[-1]
            if last_message:
                if kind == 'server' and last_message.kind == 'server':
                    last_message.update_server_message(message)
                    last_message.time = time
                
                elif last_message.sender == sender and kind != 'action':
                    last_message.update_server_message(message)
                    last_message.time = time
                    if self.network.nickname in message:
                        last_message.kind = 'highlight'
                
                else:
                    last_message.server_message_expander.set_expanded(False)
                    self.buffer.add_message_to_buffer(new_message)

            else:
                last_message.server_message_expander.set_expanded(False)
                self.buffer.add_message_to_buffer(new_message)
        
        else:
            self.buffer.add_message_to_buffer(new_message)
        
        self.window.show_all()
    
    def update_tab_complete(self, user):
        """Add/move a user to the end of the tab-complete list

        Arguments:
            user (str): the nick of the user to move.
        """
        if user in self._tab_complete:
            self._tab_complete.remove(user)
        
        self._tab_complete.append(user)
    
    def update_users(self):
        """ Updates the user list in the UI."""
        self.old_users = []
        for user in self.users:
            self.old_users.append(user)
            
        self.topic_pane.update_users()
    
    def leave(self):
        """ Remove this room from the UI."""
        self.log.debug('Removing room %s form list', self.name)
        self.buffer.destroy()
        self.topic_pane.destroy()
        self.row.destroy()
        self.notification.close()
    
    def part(self):
        """ Sends a part from this channel.
        
        Note that we don't remove the room until we receive the PART message
        from the server.
        """
        asyncio.run_coroutine_threadsafe(
            self.network.client.part(self.name, message='Leaving...'),
            loop=asyncio.get_event_loop()
        )

    # Data
    @property
    def data(self):
        """dict: A dictionary with this channel's data."""
        try:
            return self.network.client.channels[self.name]
        except KeyError:
            return {
                'users': {self.name, self.network.nickname},
                'topic': f'Private chat with {self.name}',
                'topic_by': self.network.name,
                'topic_set': Time.ctime().split()[3]
            }
    
    @property
    def users(self):
        """list: A list of users in this room."""
        users = []

        if self.kind == RoomKind.SERVER:
            users.append(self.network.nickname)
        
        elif self.kind == RoomKind.DIALOG:
            users.append(self.name)
        
        else:
            for user in self.data['users']:
                users.append(user)

        return users
    
    @property
    def ops(self):
        """:list: of str: The list of chanops in this room."""
        if self.kind == RoomKind.CHANNEL:
            try:
                return self.data['modes']['o']
            
            except KeyError:
                return []
        else:
            return []

    
    @property
    def voices(self):
        if self.kind == RoomKind.CHANNEL:
            try:
                return self.data['modes']['v']

            except KeyError:
                return []
        else:
            return []

    
    @property
    def mutes(self):
        if self.kind == RoomKind.CHANNEL:
            try: 
                return self.data['modes']['q']

            except KeyError:
                return []
        else:
            return []

    
    @property
    def tab_complete(self):
        return self._tab_complete

    @property
    def kind(self):
        """:obj:`RoomKind` The type of room this is."""
        return self._kind
    
    @kind.setter
    def kind(self, kind):
        self.log.debug('Setting room type for %s to %s', self.name, kind)
        kind = kind.upper()
        self._kind = RoomKind[kind]
        self.row.set_margins()
        self.log.debug('Set margins for %s room', kind)

    @property
    def name(self):
        """str: The name of this channel. This is displayed in the UI, and is
        the name of the channel, the network, or the user we are chatting with.
        """
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    @property
    def id(self):
        """str: The internal ID of this channel. This is used internally to 
        identify this room and it's children within the UI.

        We use the id() function to get a unique identifier for self, since this
        is guaranteed to be unique while the object exists.
        """
        return f'{self.name}-{id(self)}'
