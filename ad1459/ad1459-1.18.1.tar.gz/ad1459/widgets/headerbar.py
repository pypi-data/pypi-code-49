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

  This is the headerbar.
"""

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from .server_popup import ServerPopover

class Headerbar(Gtk.HeaderBar):
    """ The headerbar we use.
    
    Attributes:
        network_button (`Gtk.MenuButton`): The server popup button.
        server_popup (`ServerPopover`): The server popup itself.
        spinner (`Gtk.Spinner`): The network status spinner.
        appmenu (`Gtk.Popover`): The Application Menu.
        close_button (`Gtk.ModelButton`): The part/disconnect button.
        about_button (`Gtk.ModelBUtton`): The About button
    """

    def __init__(self, app):
        super().__init__()

        self.set_show_close_button(True)
        self.set_title('AD1459')
        self.set_has_subtitle(False)

        self.network_button = Gtk.MenuButton()
        network_image = Gtk.Image.new_from_icon_name(
            'network-server-symbolic',
            Gtk.IconSize.BUTTON
        )
        self.network_button.set_image(network_image)
        self.pack_start(self.network_button)

        self.server_popup = ServerPopover(app.config_file_path)
        self.server_popup.show_all()
        self.server_popup.popdown()
        self.network_button.set_popover(self.server_popup)

        self.spinner = Gtk.Spinner()
        self.pack_start(self.spinner)

        self.appmenu = Gtk.Popover()
        appmenu_grid = Gtk.Grid()
        appmenu_grid.set_margin_start(6)
        appmenu_grid.set_margin_end(6)
        appmenu_grid.set_margin_top(6)
        appmenu_grid.set_margin_bottom(6)
        self.appmenu.add(appmenu_grid)

        self.close_button = Gtk.ModelButton()
        self.close_button.set_label('Close conversation')
        appmenu_grid.attach(self.close_button, 0, 0, 1, 1)

        self.keys_button = Gtk.ModelButton()
        self.keys_button.set_label('Keyboard shortcuts')
        self.keys_button.props.action_name = 'win.show-help-overlay'
        appmenu_grid.attach(self.keys_button, 0, 1, 1, 1)

        self.about_button = Gtk.ModelButton()
        self.about_button.set_label('About AD1459')
        appmenu_grid.attach(self.about_button, 0, 2, 1, 1)

        self.appmenu.show_all()
        self.appmenu.popdown()

        appmenu_button = Gtk.MenuButton()
        appmenu_image = Gtk.Image.new_from_icon_name(
          'view-more-symbolic',
          Gtk.IconSize.BUTTON
        )
        appmenu_button.set_image(appmenu_image)
        appmenu_button.set_popover(self.appmenu)
        self.pack_end(appmenu_button)

