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

  ListBoxRows for networks/rooms.
"""

from enum import Enum

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class RoomKind(Enum):
    """ An enum to classify the type of room this is."""
    SERVER = 1
    CHANNEL = 2
    ROOM = 2
    PRIVMSG = 3
    QUERY = 3
    DIALOG = 3
    WHISPER = 3

    def __str__(self):
        """ Turn this back into a string. """
        strings = {
            1: 'network',
            2: 'channel',
            3: 'user'
        }
        return strings[self.value]

class RoomIcon(Enum):
    """ Classify the icon each RoomRow uses."""
    NONE = 1
    SERVER = 2
    MESSAGE = 3
    ACTION = 3
    NOTICE = 3
    MINE = 3
    HIGHLIGHT = 4

    def __str__(self):
        strings = {
            1: 'message-read-symbolic',
            2: 'message-server-symbolic',
            3: 'message-unread-symbolic',
            4: 'message-highlight-symbolic'
        }
        return strings[self.value]

def sort_by_server(row1, row2):
    """Sorts the rows alphabetically by their network name."""
    if row1.room.network.name < row2.room.network.name:
        return -1
    
    else:
        return 1

def sort_by_room(row1, row2):
    """ Sorts the rows alphabetically by room name."""
    if row1.room.name < row2.room.name:
        return -1
    
    else:
        return 1

def room_row_sort(row1, row2, *user_data):
    """ Tells whether row1 should be before row2 or not

    Arguments:
        row1 (:obj:`RoomRow`): The first row to compare
        row2 (:obj:`RoomRow`): The second row to compare
        user_data (:obj:`object or None): user data
    
    Returns:
        -1 if row1 should go before row2.
        0  if they are equal and the order doesn't matter. 
        1  if row1 should go after row2.
    """
    
    if row1.kind == RoomKind.SERVER:
        if row2.kind == RoomKind.SERVER:
            return sort_by_server(row1, row2)
        else:
            
            if row2.room in row1.room.network.rooms:
                return -1

            else:
                return sort_by_server(row1, row2)

    elif row1.kind == RoomKind.CHANNEL:
        if row2.kind == RoomKind.SERVER:
            if row1.room in row2.room.network.rooms:
                return 1
            
            else:
                return sort_by_server(row1, row2)

        elif row2.kind == RoomKind.CHANNEL:
            if row1.room in row2.room.network.rooms:
                return sort_by_room(row1, row2)
            
            else:
                return sort_by_server(row1, row2)

        elif row2.kind == RoomKind.DIALOG:
            if row1.room in row2.room.network.rooms:
                return -1
            
            else:
                return sort_by_server(row1, row2)

    elif row1.kind == RoomKind.DIALOG:
        if row2.kind == RoomKind.SERVER or row2.kind == RoomKind.CHANNEL:
            if row1.room in row2.room.network.rooms:
                return 1

            else:
                
                return sort_by_server(row1, row2)

        if row2.kind == RoomKind.DIALOG:
            if row1.room in row2.room.network.rooms:
                return sort_by_room(row1, row2)
            
            else:
                
                return sort_by_server(row1, row2)

class RoomRow(Gtk.ListBoxRow):
    """ A dedicated ListBoxRow for representing a room in the Room List.
    
    Attributes:
        room_name (str): The name of this room.
        kind (RoomKind Enum): The type of room this is.
    """

    def __init__(self, room):
        super().__init__()
        self.room = room
        self._icon = RoomIcon.NONE
        self.set_can_focus(False)

        grid = Gtk.Grid()
        grid.set_column_spacing(6)
        grid.set_margin_top(3)
        grid.set_margin_bottom(3)
        grid.set_margin_start(3)
        grid.set_margin_end(3)
        self.add(grid)

        self.room_label = Gtk.Label()
        self.room_label.set_text(self.room.name)
        grid.attach(self.room_label, 0, 0, 1, 1)

        self.unread_indicator = Gtk.Image.new_from_icon_name(
            'radio-symbolic',
            Gtk.IconSize.SMALL_TOOLBAR            
        )
        grid.attach(self.unread_indicator, 1, 0, 1, 1)

    # Methods
    def set_margins(self):
        """Sets the margins on self depending on what type of room we are."""
        print(self.room.kind)
        if self.room.kind == RoomKind.SERVER:
            self.set_margin_top(12) 
            self.set_margin_start(0)
        elif self.room.kind == RoomKind.CHANNEL: 
            self.set_margin_top(0)
            self.set_margin_start(12)
        elif self.room.kind == RoomKind.DIALOG:
            self.set_margin_top(0)
            self.set_margin_start(18)
        else:
            self.set_margin_top(0)
            self.set_margin_start(0)

    def set_icon(self, icon_name):
        self.unread_indicator.set_from_icon_name(
            icon_name, Gtk.IconSize.SMALL_TOOLBAR
        )

    # Data
    @property
    def kind(self):
        """Easier compatibility with sort func."""
        return self.room.kind
    
    @property
    def icon(self):
        """`RoomIcon`: The icon that this row should have."""
        return self._icon
    
    @icon.setter
    def icon(self, icon):
        try:
            _icon = str(icon).upper()
            self._icon = RoomIcon[_icon]
        
        except AttributeError:
            self._icon = RoomIcon(icon)
        
        self.unread_indicator.set_from_icon_name(
            str(self._icon),
            Gtk.IconSize.SMALL_TOOLBAR
        )
   