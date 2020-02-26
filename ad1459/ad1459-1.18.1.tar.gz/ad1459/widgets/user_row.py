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

import asyncio

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from .right_click_menus import UserRowMenu

class UserRow(Gtk.ListBoxRow):
    """ A row for a user in the user list.

    The attributes for this class are stored in the label widget for this row.

    Attributes:
        nick (str): This user's nickname.
    """

    def __init__(self, room):
        super().__init__()
        self.room = room
        grid = Gtk.Grid()
        grid.set_column_spacing(6)
        grid.set_margin_top(3)
        grid.set_margin_bottom(3)
        grid.set_margin_start(3)
        grid.set_margin_end(3)

        self.context_menu = UserRowMenu(self.room, self)
        self.context_menu.set_relative_to(self)
        self.context_menu.set_modal(True)

        event = Gtk.EventBox()
        self.add(event)

        event.add(grid)

        event.connect('button-press-event', self.on_user_row_button_release)

        self.status_image = Gtk.Image.new_from_icon_name(
            'radio-symbolic',
            Gtk.IconSize.SMALL_TOOLBAR
        )
        self.status_image.props.opacity = 0
        grid.attach(self.status_image, 0, 0, 1, 1)

        self.user_label = Gtk.Label()
        grid.attach(self.user_label, 1, 0, 1, 1)

        self._modes = []
    
    def get_voice(self):
        if 'v' in self.modes:
            return True
        return False
    
    def get_op(self):
        if 'o' in self.modes:
            return True
        return False
    
    def get_mute(self):
        if 'q' in self.modes:
            return True
        return False
    
    # Internal Handlers
    def on_user_row_button_release(self, widget, event, data=None):
        if event.button == 3:
            print(f'User row {self.nick} right-clicked')
            self.context_menu.popup()
            asyncio.run_coroutine_threadsafe(
                self.context_menu.update_info(self.nick),
                loop=asyncio.get_event_loop()
            )
    
    # Data
    @property
    def nick(self):
        """str: The user's nickname."""
        return self.user_label.get_text()
    
    @nick.setter
    def nick(self, nick):
        self.user_label.set_text(nick)

    @property
    def modes(self):
        """:list: of str: The current user modes for this user"""
        try:
            return self._modes
        except AttributeError:
            return []
    
    @modes.setter
    def modes(self, modes):
        self._modes = modes
        self.status_image.set_opacity(0)

        if 'q' in self._modes:
            self.status_image.set_from_icon_name(
                'user-mute-symbolic',
                Gtk.IconSize.SMALL_TOOLBAR
            )
            self.status_image.set_opacity(0.5)
        
        if 'v' in self._modes:
            self.status_image.set_from_icon_name(
                'user-voice-symbolic',
                Gtk.IconSize.SMALL_TOOLBAR
            )
            self.status_image.set_opacity(1)

        if 'o' in self._modes:
            self.status_image.set_from_icon_name(
                'user-op-symbolic',
                Gtk.IconSize.SMALL_TOOLBAR
            )
            self.status_image.set_opacity(1)
    
    @property
    def op(self):
        """bool: True if user is chanop."""
        if 'o' in self.modes:
            return True
        
    @property
    def voice(self):
        if 'v' in self.modes and not 'o' in self.modes:
            return True
    
    @property
    def mute(self):
        if 'q' in self.modes and not 'o' in self.modes and not 'v' in self.modes:
            return True
    
    @property
    def nomodes(self):
        if not 'q' in self.modes and not 'o' in self.modes and not 'v' in self.modes:
            return True
