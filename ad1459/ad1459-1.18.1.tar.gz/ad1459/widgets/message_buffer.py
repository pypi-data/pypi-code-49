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

  A buffer full of messages.
"""

import logging

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MessageBuffer(Gtk.ScrolledWindow):
    """ A buffer to display messages.

    This should be added as a child of a Gtk.Stack in the main window.
    
    Attributes:
        room (`Room`): The room this buffer belongs to.
    """

    def __init__(self, room):
        super().__init__()
        self.room = room

        self.list_box = Gtk.ListBox()
        self.list_box.set_vexpand(True)
        self.list_box.set_hexpand(True)
        self.list_box.connect('size-allocate', self.scroll_to_bottom)

        self.adj = self.get_vadjustment()
        self.adj.connect('value-changed', self.on_window_scroll)
        self.add(self.list_box)

    def add_message_to_buffer(self, message):
        """Adds a message into the buffer."""
        self.list_box.add(message)

        # Scroll to the bottom if this is our own message.
        if message.sender == self.room.network.nickname:
            self.scroll_to_bottom(self.list_box)
    
    def on_window_scroll(self, widget, data=None):
        """value-changed signal handler for the window adjustment.
        
        This is used to detect when the user scrolls up, so that we can 
        disconnect the `scroll_to_bottom` handler when we get a new message.
        """
        adj = self.get_vadjustment()
        max_value = adj.get_upper() - adj.get_page_size()

        if adj.get_value() < max_value:
            try:
                self.list_box.disconnect_by_func(self.scroll_to_bottom)
            
            except TypeError:
                pass
        
        else:
            try:
                self.list_box.disconnect_by_func(self.scroll_to_bottom)
            
            except TypeError:
                pass

            self.list_box.connect('size-allocate', self.scroll_to_bottom)

    def scroll_to_bottom(self, widget, data=None):
        """Scroll to the bottom of the buffer."""
        adj = self.get_vadjustment()
        max_value = adj.get_upper() - adj.get_page_size()
        adj.set_value(max_value)