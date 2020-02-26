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
from .room_row import room_row_sort

class RoomSwitcher(Gtk.Grid):
    """ The room switcher sidebar content in the main window. 

    This contains room rows for all of the currently open rooms, and allows the
    user to click on them to switch to a different room.
    """

    def __init__(self, app):
        super().__init__()
        self.app = app

        window = Gtk.ScrolledWindow()
        window.set_hexpand(True)
        window.set_vexpand(True)
        self.attach(window, 0, 0, 1, 1)

        self.switcher = Gtk.ListBox()
        self.switcher.set_hexpand(True)
        self.switcher.set_vexpand(True)
        self.switcher.set_sort_func(room_row_sort)
        window.add(self.switcher)
    
    def add_row(self, row):
        """ Adds a row to the ListBox.

        Arguments:
            row (:obj:`RoomRow`): A Room Row to add to the listbox.
        """
        self.switcher.insert(row, 0)
    
    def remove_row(self, row):
        """ Removes a row from the ListBox.

        Arguments:
            row (:obj:`RoomRow`): The row to remove
        """
        try:
            row.destroy()

        except AttributeError:
            pass

        self.switcher.invalidate_sort()
    
    def invalidate_sort(self):
        """ proxy for self.switcher.invalidate_sort()"""
        self.switcher.invalidate_sort()
    
    def get_active_room(self):
        """Gets the currently selected Room.

        Returns:
            a :obj:`Room` for the currently selected row
        """
        room = self
        room.network = ""
        return room

