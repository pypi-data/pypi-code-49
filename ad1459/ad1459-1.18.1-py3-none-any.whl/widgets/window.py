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

  This file is an application window.
"""

import logging

import gi
gi.require_versions(
    {
        'Gtk': '3.0',
        'Gdk': '3.0'
    }
)
from gi.repository import Gtk, Gdk

from .. import formatting
from .about import AboutDialog
from .headerbar import Headerbar
from .irc_entry import IrcEntry
from .room_switcher import RoomSwitcher
from .server_popup import ServerPopover

class Ad1459Window(Gtk.ApplicationWindow):
    """ This is a window for AD1459. 
    
    This contains the overall layout as well as most of the general controls for
    the app.

    Attributes:
        active_room (:obj:`Room`): The currently active room.
        focused (bool): Whether the window is currently focused or not.
    """

    def __init__(self, app):
        self.log = logging.getLogger('ad1459.window')
        self.log.debug('Creating window')

        self.app = app
        self.parser = formatting.Parser()

        super().__init__()
        self.set_default_size(1000, 600)

        self.header = Headerbar(self.app)
        self.set_titlebar(self.header)

        self.add_help_overlay()

        self.main_pane = Gtk.HPaned()
        self.main_pane.set_position(200)
        self.add(self.main_pane)

        channel_grid = Gtk.Grid()
        channel_grid.set_hexpand(True)
        channel_grid.set_vexpand(True)
        self.main_pane.add2(channel_grid)

        switcher_grid = Gtk.Grid()
        switcher_grid.set_hexpand(True)
        switcher_grid.set_vexpand(True)
        self.main_pane.add1(switcher_grid)

        self.switcher = RoomSwitcher(self.app)
        switcher_grid.attach(self.switcher, 0, 0, 1, 1)

        join_bar = Gtk.ActionBar()
        switcher_grid.attach(join_bar, 0, 1, 1, 1)

        self.join_entry = Gtk.Entry()
        self.join_entry.set_width_chars(1)
        self.join_entry.set_hexpand(True)
        self.join_entry.set_placeholder_text('Join channel')
        self.join_entry.set_icon_from_icon_name(
            Gtk.EntryIconPosition.SECONDARY, 'list-add-symbolic'
        )
        self.join_entry.set_icon_activatable(
            Gtk.EntryIconPosition.SECONDARY, True
        )
        join_bar.pack_start(self.join_entry)

        entry_grid = Gtk.ActionBar()
        channel_grid.attach(entry_grid, 0, 1, 1, 1)
        
        self.irc_entry = IrcEntry(self)
        self.nick_button = Gtk.Button.new_with_label('nickname')
        self.send_button = Gtk.Button.new_from_icon_name(
            'mail-send-symbolic', Gtk.IconSize.BUTTON
        )

        self.nick_button.set_halign(Gtk.Align.START)
        self.send_button.set_halign(Gtk.Align.END)

        Gtk.StyleContext.add_class(
            self.nick_button.get_style_context(), 'flat'
        )
        Gtk.StyleContext.add_class(
            self.send_button.get_style_context(), 'suggested-action'
        )

        entry_grid.pack_start(self.nick_button)
        entry_grid.pack_start(self.irc_entry)
        entry_grid.pack_start(self.send_button)

        self.channel_pane = Gtk.HPaned()
        self.channel_pane.set_position(600)
        channel_grid.attach(self.channel_pane, 0, 0, 1, 1)

        self.message_stack = Gtk.Stack()
        self.message_stack.set_hexpand(True)
        self.message_stack.set_vexpand(True)
        self.message_stack.set_transition_type(Gtk.StackTransitionType.CROSSFADE)
        self.message_stack.set_transition_duration(100)
        self.channel_pane.pack1(self.message_stack, True, True)

        self.topic_stack = Gtk.Stack()
        self.topic_stack.set_hexpand(True)
        self.topic_stack.set_vexpand(True)
        self.topic_stack.set_transition_type(Gtk.StackTransitionType.CROSSFADE)
        self.topic_stack.set_transition_duration(100)
        self.channel_pane.pack2(self.topic_stack, False, False)

        self.irc_entry.grab_focus_without_selecting()

        self.recents = []

        self.connect('focus-in-event', self.on_focus_changed)
    
    # Methods
    def add_help_overlay(self):
        keys_window = Gtk.ShortcutsWindow()
        main_section = Gtk.ShortcutsSection()
        main_section.props.section_name = 'AD1459 Shortcuts'
        keys_window.add(main_section)
        
        entry_group = Gtk.ShortcutsGroup()
        entry_group.props.title = 'Entry Shortcuts'
        main_section.add(entry_group)
        
        tab_shortcut = Gtk.ShortcutsShortcut()
        tab_shortcut.props.accelerator = 'Tab'
        tab_shortcut.props.title = (
            'Auto-complete nicknames'
        )
        entry_group.add(tab_shortcut)
        
        room_recent_shortcut = Gtk.ShortcutsShortcut()
        room_recent_shortcut.props.accelerator = 'Up Down'
        room_recent_shortcut.props.title = (
            'Move through the recently sent messages for the current channel'
        )
        entry_group.add(room_recent_shortcut)
        
        win_recent_shortcut = Gtk.ShortcutsShortcut()
        win_recent_shortcut.props.accelerator= '<ctl>Up <clt>Down'
        win_recent_shortcut.props.title = (
            'Move through the recently sent messages from all channels'
        )
        entry_group.add(win_recent_shortcut)

        self.set_help_overlay(keys_window)
    
    # Internal Handlers
    def on_focus_changed(self, window, data=None):
        """ Unset the unread indicator for the current room when we gain focus.
        """
        try:
            room = self.message_stack.get_visible_child().room
        except AttributeError:
            return
        self.log.debug('Unsetting unread indicator for %s', room.name)
        room.row.icon = 'none'

    # Data
    @property
    def active_room(self):
        """ Room: The currently active room."""
        room = self.message_stack.get_visible_child().room
        return room

    @property
    def focused(self):
        """bool: Whether or not the window has focus."""
        if self.props.is_active:
            return True
        
        return False
