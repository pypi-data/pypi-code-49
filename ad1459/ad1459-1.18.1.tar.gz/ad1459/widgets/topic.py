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

  The topic pane contents.
"""

import logging

import gi
gi.require_versions(
    {
        'Gtk': '3.0'
    }
)
from gi.repository import Gtk, GLib

from .user_row import UserRow
from .room_row import RoomKind

class TopicPane(Gtk.Grid):
    """ The right-sidebar of the UI, containing the topic and the User List."""

    def __init__(self, room):
        super().__init__()
        self.room = room
        self.log = logging.getLogger('ad1459.topic')
        self.topic_expander = Gtk.Expander()
        self.topic_expander.set_margin_top(6)
        self.topic_expander.set_margin_end(3)
        self.topic_expander.set_label_fill(True)
        self.topic_expander.connect('notify::expanded', self.show_hide_topic)
        self.attach(self.topic_expander, 0, 0, 1, 1)

        # Set Expander Label
        self.exp_label = Gtk.Label()
        self.exp_label.set_line_wrap(True)
        self.exp_label.set_xalign(0)
        self.exp_label.set_margin_start(3)
        self.exp_label.set_margin_end(3)
        self.topic_expander.set_label_widget(self.exp_label)

        self.revealer = Gtk.Revealer()
        self.revealer.set_margin_start(18)
        self.revealer.set_margin_end(3)
        self.revealer.set_transition_type(Gtk.RevealerTransitionType.SLIDE_DOWN)
        self.attach(self.revealer, 0, 1, 1, 1)

        self.topic_label = Gtk.Label()
        self.topic_label.set_margin_start(6)
        self.topic_label.set_margin_end(6)
        self.topic_label.set_margin_top(3)
        self.topic_label.set_margin_bottom(6)
        self.topic_label.set_xalign(0)
        self.topic_label.set_line_wrap(True)
        self.revealer.add(self.topic_label)

        separator = Gtk.Separator.new(Gtk.Orientation.HORIZONTAL)
        separator.set_hexpand(True)
        self.attach(separator, 0, 2, 1, 1)

        user_window = Gtk.ScrolledWindow()
        user_window.set_hexpand(True)
        user_window.set_vexpand(True)
        self.attach(user_window, 0, 3, 1, 1)

        self.user_list = Gtk.ListBox()
        self.user_list.set_hexpand(True)
        self.user_list.set_vexpand(True)
        self.user_list.set_activate_on_single_click(False)
        self.user_list.set_sort_func(sort_users)
        self.user_list.connect(
            'row-activated',
            self.on_user_row_activated,
            self.room.window
        )
        user_window.add(self.user_list)

        self.update_topic()
    
    def update_topic(self):
        """Update the channel topic."""
        self.log.debug('Updating topic for %s', self.room.id)

        try:
            topic_expander_label = '<small>Set by '
            topic_by = GLib.markup_escape_text(self.room.data['topic_by'])
            topic_expander_label += f'<i>{topic_by}</i> on '
            topic_expander_label += f'<i>{self.room.data["topic_set"]}</i>:</small>'
            topic_text = GLib.markup_escape_text(self.room.data['topic'])
            topic_text = self.room.window.parser.parse_text(topic_text)
            topic_text = self.room.window.parser.hyperlinks(topic_text)
            self.topic_expander.set_sensitive(True)
            self.topic_expander.set_expanded(True)
        
        except (KeyError, TypeError):
            topic_expander_label = "No topic set"
            topic_text = ''
            self.topic_expander.set_sensitive(False)
            self.topic_expander.set_expanded(False)

        self.exp_label.set_markup(topic_expander_label)
        self.topic_label.set_markup(f'<small>{topic_text}</small>')

    def update_users(self):
        """Updates this room's user list."""
        curr_users = self.user_list.get_children()
        
        for user in curr_users:
            GLib.idle_add(user.destroy)

        for user in self.room.users:
            new_user = UserRow(self.room)
            new_user.nick = user
            self.user_list.add(new_user)
            modes = []
            
            if user in self.room.mutes:
                modes.append('q')
            
            if user in self.room.voices:
                modes.append('v')

            if user in self.room.ops:
                modes.append('o')
            
            new_user.modes = modes
            
            if user == 'Miga':
                self.log.debug('Miga mdoes: %s', new_user.modes)
        
        self.room.window.show_all()
        self.user_list.invalidate_sort()
    
    # Internal Handlers
    def show_hide_topic(self, expander, data=None):
        """ Shows or hides the topic.

        This is synced to the `expanded` property of `expander`.
        """
        self.revealer.props.reveal_child = expander.get_expanded()
    
    def on_user_row_activated(self, list_box, row, window):
        """ `row-activated` handler for the list bow. 

        This opens a PM room with the selected user.
        """
        user = row.nick
        network = row.room.network
        room = network.get_room_for_name(user)
        window.message_stack.set_visible_child_name(room.id)
        window.topic_stack.set_visible_child_name(room.id)
        window.irc_entry.grab_focus_without_selecting()
        window.nick_button.set_label(network.nickname)
        window.switcher.switcher.select_row(room.row)

def sort_users(row1, row2, *user_data):
    """ Sorts the users for the user list.

    Arguments:
        row1: The first user row to compare
        row2: The second user row to compare
    
    Returns:
        -1 if row1 should go above row2
        1 if row1 should go below row2
    """
    if row1.mute:
        if row2.mute:
            return sort_users_alpha(row1, row2)
        
        else:
            return 1
    
    if row1.voice:
        if row2.voice:
            return sort_users_alpha(row1, row2)
        
        elif row2.op:
            return 1
        
        else:
            return -1
    
    if row1.op:
        if row2.op:
            return sort_users_alpha(row1, row2)
        
        else:
            return -1
    
    if row1.nomodes:
        if row2.nomodes:
            return sort_users_alpha(row1, row2)
        
        elif row2.mute:
            return -1
        
        else:
            return 1

def sort_users_alpha(row1, row2):
    """ Sorts the users alphabetically by nick."""

    if row1.nick.upper() < row2.nick.upper():
        return -1
    else:
        return 1